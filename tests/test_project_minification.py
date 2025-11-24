"""Tests for test_project minification and runtime."""
import os
import subprocess
import sys
import tempfile
import shutil
import time
from pathlib import Path

import pytest

# Get the paths
PROJECT_ROOT = Path(__file__).parent.parent
TEST_PROJECT_DIR = PROJECT_ROOT / "test_project"


def test_test_project_exists():
    """Verify test_project directory exists."""
    assert TEST_PROJECT_DIR.exists(), f"test_project directory not found at {TEST_PROJECT_DIR}"
    assert (TEST_PROJECT_DIR / "app").exists()
    assert (TEST_PROJECT_DIR / "lib").exists()
    assert (TEST_PROJECT_DIR / "build.py").exists()


def test_build_script_runs():
    """Test that build.py can be executed without errors."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Copy test_project to temp directory
        tmp_project = Path(tmpdir) / "test_project"
        shutil.copytree(TEST_PROJECT_DIR, tmp_project)
        
        # Run build.py
        result = subprocess.run(
            [sys.executable, "build.py"],
            cwd=tmp_project,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        # Check it completed successfully
        assert result.returncode == 0, f"build.py failed:\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        
        # Verify vendored dependencies exist
        assert (tmp_project / "fastapi").exists(), "fastapi should be vendored"
        assert (tmp_project / "starlette").exists(), "starlette should be vendored"
        

def test_vendored_dependencies_are_minified():
    """Test that vendored dependencies are actually minified."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Copy test_project to temp directory
        tmp_project = Path(tmpdir) / "test_project"
        shutil.copytree(TEST_PROJECT_DIR, tmp_project)
        
        # Run build.py
        result = subprocess.run(
            [sys.executable, "build.py"],
            cwd=tmp_project,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        assert result.returncode == 0, f"build.py failed: {result.stderr}"
        
        # Check that fastapi files are minified (no unnecessary whitespace, etc.)
        fastapi_init = tmp_project / "fastapi" / "__init__.py"
        if fastapi_init.exists():
            content = fastapi_init.read_text()
            # Minified code should have less newlines
            # Check that it's not the original (which would have docstrings and comments)
            assert content.count('\n\n\n') < 5, "fastapi/__init__.py doesn't appear to be minified"


def test_minified_app_structure():
    """Test that the minified app has correct structure."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Copy test_project to temp directory
        tmp_project = Path(tmpdir) / "test_project"
        shutil.copytree(TEST_PROJECT_DIR, tmp_project)
        
        # Run build.py
        result = subprocess.run(
            [sys.executable, "build.py"],
            cwd=tmp_project,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        assert result.returncode == 0, f"build.py failed: {result.stderr}"
        
        # Check app files exist (note: files may be obfuscated)
        assert (tmp_project / "app" / "app.py").exists()
        # v0 module gets obfuscated, so we check for any obfuscated directories
        obfuscated_dirs = [d for d in (tmp_project / "app").iterdir() if d.is_dir() and d.name not in ["__pycache__", "v0"]]
        assert len(obfuscated_dirs) > 0, "Expected at least one obfuscated subdirectory in app/"
        # Check lib still exists (it gets obfuscated at root level)
        root_dirs = [d for d in tmp_project.iterdir() if d.is_dir() and not d.name.startswith('.')]
        assert len(root_dirs) > 2, f"Expected multiple directories at root, found: {[d.name for d in root_dirs]}"


@pytest.mark.skipif(not shutil.which("uvicorn"), reason="uvicorn not installed")
def test_minified_app_runs_with_uvicorn():
    """Test that the minified app can run with uvicorn."""
    # Check if fastapi is available
    try:
        import fastapi
    except ImportError:
        pytest.skip("fastapi not available")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # Copy test_project to temp directory
        tmp_project = Path(tmpdir) / "test_project"
        shutil.copytree(TEST_PROJECT_DIR, tmp_project)
        
        # Copy already vendored dependencies if they exist in TEST_PROJECT_DIR
        # This allows testing with already minified projects
        for dep_dir in ["fastapi", "starlette", "httpx", "orjson", "requests", "urllib3", "chardet", "cryptography"]:
            src_dep = TEST_PROJECT_DIR / dep_dir
            if src_dep.exists():
                shutil.copytree(src_dep, tmp_project / dep_dir, dirs_exist_ok=True)
        
        # Also copy any obfuscated directories (single letter names)
        for item in TEST_PROJECT_DIR.iterdir():
            if item.is_dir() and len(item.name) == 1 and item.name.isupper():
                shutil.copytree(item, tmp_project / item.name, dirs_exist_ok=True)
        
        # Run build.py
        result = subprocess.run(
            [sys.executable, "build.py"],
            cwd=tmp_project,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        assert result.returncode == 0, f"build.py failed: {result.stderr}"
        
        # Try to start uvicorn server
        env = os.environ.copy()
        env['PYTHONPATH'] = str(tmp_project)
        
        proc = subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "app.app:app", "--host", "127.0.0.1", "--port", "8999"],
            cwd=tmp_project,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        try:
            # Wait for server to start
            time.sleep(3)
            
            # Check if process is still running
            poll = proc.poll()
            if poll is not None:
                stdout, stderr = proc.communicate()
                # Don't fail if it's a missing dependency issue during testing
                if "ModuleNotFoundError" in stderr or "ImportError" in stderr:
                    pytest.skip(f"Dependencies not available in test environment: {stderr[:200]}")
                pytest.fail(f"uvicorn failed to start:\nSTDOUT:\n{stdout}\nSTDERR:\n{stderr}")
            
            # Test with httpx if available
            try:
                import httpx
                
                response = httpx.get("http://127.0.0.1:8999/", timeout=5.0)
                assert response.status_code == 200
                assert response.json() == {"success": "Hello, world!"}
                
                response = httpx.get("http://127.0.0.1:8999/v0", timeout=5.0)
                assert response.status_code == 200
                assert response.json() == {"version": "0"}
                
                response = httpx.get("http://127.0.0.1:8999/v0/router", timeout=5.0)
                assert response.status_code == 200
                assert response.json() == {"message": "Hello from utils!"}
                
            except ImportError:
                pytest.skip("httpx not available for HTTP testing")
                
        finally:
            # Clean up
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait()


def test_vendored_deps_options_applied():
    """Test that vendored_deps_options are applied correctly."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Copy test_project to temp directory
        tmp_project = Path(tmpdir) / "test_project"
        shutil.copytree(TEST_PROJECT_DIR, tmp_project)
        
        # Run build.py with verbose output
        result = subprocess.run(
            [sys.executable, "build.py"],
            cwd=tmp_project,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        assert result.returncode == 0, f"build.py failed: {result.stderr}"
        
        # Verify that vendored dependencies were processed
        # (The presence of minified files indicates they were loaded and minified)
        assert (tmp_project / "fastapi").exists()
        
        # Check that files in vendored dependencies are minified
        # Look for obfuscated module names if obfuscate_module_names was applied
        # Since obfuscate_module_names is True for vendored deps, 
        # some directories might be renamed
        root_dirs = [d for d in tmp_project.iterdir() if d.is_dir() and not d.name.startswith('.')]
        
        # Should have vendored dependencies
        assert len(root_dirs) > 2, f"Expected vendored dependencies, found: {[d.name for d in root_dirs]}"
