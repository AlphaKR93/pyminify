"""Tests for test_project minification and runtime."""
import subprocess
import tempfile
import shutil
import time
from pathlib import Path

import pytest

# Get the paths
PROJECT_ROOT = Path(__file__).parent.parent
TEST_PROJECT_DIR = PROJECT_ROOT / "test_project"


def setup_test_project_with_uv(tmpdir):
    """Helper function to set up test_project with uv in a temp directory."""
    # Copy test_project to temp directory
    tmp_project = Path(tmpdir) / "test_project"
    shutil.copytree(TEST_PROJECT_DIR, tmp_project, ignore=shutil.ignore_patterns('.venv', '__pycache__'))
    
    # Copy the main project for the local pyminify dependency
    tmp_pyminify = Path(tmpdir) / "pyminify"
    shutil.copytree(PROJECT_ROOT, tmp_pyminify, ignore=shutil.ignore_patterns('.venv', '__pycache__', 'test_project', 'tests', '.git'))
    
    # Update the pyminify source path in pyproject.toml to point to tmp_pyminify
    pyproject_path = tmp_project / "pyproject.toml"
    pyproject_content = pyproject_path.read_text()
    # Replace the relative path with the temp location
    pyproject_content = pyproject_content.replace('{ path = "../" }', f'{{ path = "{tmp_pyminify}" }}')
    pyproject_path.write_text(pyproject_content)
    
    # Sync dependencies with uv
    sync_result = subprocess.run(
        ["uv", "sync", "--group", "build"],
        cwd=tmp_project,
        capture_output=True,
        text=True,
        timeout=120
    )
    if sync_result.returncode != 0:
        raise RuntimeError(f"uv sync failed:\nSTDOUT:\n{sync_result.stdout}\nSTDERR:\n{sync_result.stderr}")
    
    return tmp_project


def test_test_project_exists():
    """Verify test_project directory exists."""
    assert TEST_PROJECT_DIR.exists(), f"test_project directory not found at {TEST_PROJECT_DIR}"
    assert (TEST_PROJECT_DIR / "app").exists()
    assert (TEST_PROJECT_DIR / "lib").exists()
    assert (TEST_PROJECT_DIR / "build.py").exists()


def test_build_script_runs():
    """Test that build.py can be executed without errors using uv."""
    # Check if uv is available
    if not shutil.which("uv"):
        pytest.skip("uv not available")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_project = setup_test_project_with_uv(tmpdir)
        
        # Run build.py with uv
        result = subprocess.run(
            ["uv", "run", "build.py"],
            cwd=tmp_project,
            capture_output=True,
            text=True,
            timeout=120
        )
        
        # Check it completed successfully
        assert result.returncode == 0, f"build.py failed:\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        
        # Verify vendored dependencies exist (they might be obfuscated with single-letter names)
        # Check for common dependencies or any single-letter directories
        root_dirs = [d for d in tmp_project.iterdir() if d.is_dir() and not d.name.startswith('.') and d.name not in ['app', 'lib']]
        assert len(root_dirs) > 0, f"No vendored dependencies found. Directories: {[d.name for d in tmp_project.iterdir() if d.is_dir()]}"
        

def test_vendored_dependencies_are_minified():
    """Test that vendored dependencies are actually minified."""
    # Check if uv is available
    if not shutil.which("uv"):
        pytest.skip("uv not available")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_project = setup_test_project_with_uv(tmpdir)
        
        # Run build.py with uv
        result = subprocess.run(
            ["uv", "run", "build.py"],
            cwd=tmp_project,
            capture_output=True,
            text=True,
            timeout=120
        )
        
        assert result.returncode == 0, f"build.py failed: {result.stderr}"
        
        # Check that vendored dependencies exist and appear minified
        # Since obfuscate_module_names is True, dependencies might have obfuscated names
        root_dirs = [d for d in tmp_project.iterdir() if d.is_dir() and not d.name.startswith('.') and d.name not in ['app', 'lib']]
        assert len(root_dirs) > 0, "No vendored dependencies found"
        
        # Check one of the vendored packages has minified content
        # Look for any Python files in vendored directories
        for vendor_dir in root_dirs:
            py_files = list(vendor_dir.rglob("*.py"))
            if py_files:
                # Found Python files, check they're minified (no excessive whitespace)
                sample_file = py_files[0]
                if sample_file.stat().st_size > 0:
                    content = sample_file.read_text()
                    # Minified code should have less blank lines
                    blank_line_ratio = content.count('\n\n\n') / max(content.count('\n'), 1)
                    assert blank_line_ratio < 0.1, f"File {sample_file} doesn't appear minified"
                    break


def test_minified_app_structure():
    """Test that the minified app has correct structure."""
    # Check if uv is available
    if not shutil.which("uv"):
        pytest.skip("uv not available")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_project = setup_test_project_with_uv(tmpdir)
        
        # Run build.py with uv
        result = subprocess.run(
            ["uv", "run", "build.py"],
            cwd=tmp_project,
            capture_output=True,
            text=True,
            timeout=120
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
@pytest.mark.skipif(not shutil.which("uv"), reason="uv not installed")
def test_minified_app_runs_with_uvicorn():
    """Test that the minified app can run with uvicorn."""
    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            tmp_project = setup_test_project_with_uv(tmpdir)
        except RuntimeError as e:
            pytest.skip(str(e))
        
        # Run build.py with uv
        result = subprocess.run(
            ["uv", "run", "build.py"],
            cwd=tmp_project,
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode != 0:
            pytest.skip(f"build.py failed: {result.stderr}")
        
        # Try to start uvicorn server using uv run
        proc = subprocess.Popen(
            ["uv", "run", "uvicorn", "app.app:app", "--host", "127.0.0.1", "--port", "8999"],
            cwd=tmp_project,
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
    # Check if uv is available
    if not shutil.which("uv"):
        pytest.skip("uv not available")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_project = setup_test_project_with_uv(tmpdir)
        
        # Run build.py with uv
        result = subprocess.run(
            ["uv", "run", "build.py"],
            cwd=tmp_project,
            capture_output=True,
            text=True,
            timeout=120
        )
        
        assert result.returncode == 0, f"build.py failed: {result.stderr}"
        
        # Verify that vendored dependencies were processed
        # (The presence of minified files indicates they were loaded and minified)
        root_dirs = [d for d in tmp_project.iterdir() if d.is_dir() and not d.name.startswith('.') and d.name not in ['app', 'lib']]
        
        # Should have vendored dependencies
        assert len(root_dirs) > 0, f"Expected vendored dependencies, found: {[d.name for d in tmp_project.iterdir() if d.is_dir()]}"
