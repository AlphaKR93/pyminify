"""
Dependency collector for tree shaking and vendoring external dependencies.
"""

from __future__ import annotations

import ast
import importlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from collections import deque


class DependencyCollector:
    """
    Collects and vendors external dependencies used by a Python project.

    Supports two modes:
    1. AST-based discovery: Parse imports from source files (tree shaking)
    2. Package manager-based: Use uv/pip to get all installed packages
    """

    def __init__(self, verbose: bool = False, use_package_manager: bool = True):
        """
        Initialize the dependency collector.

        :param verbose: If True, print debug information during collection
        :param use_package_manager: If True, use uv/pip to discover dependencies (recommended)
        """
        self.verbose = verbose
        self.use_package_manager = use_package_manager
        self.visited_modules: set[str] = set()
        self.to_process: deque[str] = deque()
        self.module_paths: dict[str, str] = {}  # module_name -> file_path

        # Packages that should never be vendored (dev tools, testing, etc.)
        self.excluded_packages = {
            "pytest",
            "pytest_cov",
            "coverage",
            "nose",
            "unittest2",
            "mock",
            "debugpy",
            "pydevd",
            "pydev",
            "pdb",
            "ipdb",
            "pudb",
            "mypy",
            "pyright",
            "basedpyright",
            "pylint",
            "flake8",
            "ruff",
            "black",
            "setuptools",
            "pip",
            "wheel",
            "build",
            "twine",
            "sphinx",
            "readthedocs",
            "mkdocs",
            "jupyter",
            "ipython",
            "notebook",
            "_pydev",
            "_pydevd",
            "pydev_ipython",
            "pydev_jupyter",
        }

        # Use sys.stdlib_module_names for Python 3.10+ (recommended: Python 3.12+)
        # For older Python versions, basic stdlib detection via importlib will still work
        if hasattr(sys, "stdlib_module_names"):
            self.stdlib_modules = sys.stdlib_module_names
        else:
            # Minimal fallback for common stdlib modules on older Python
            # Note: This is not comprehensive. Consider upgrading to Python 3.10+
            self.stdlib_modules = {
                "abc",
                "aifc",
                "argparse",
                "array",
                "ast",
                "asynchat",
                "asyncio",
                "asyncore",
                "atexit",
                "audioop",
                "base64",
                "bdb",
                "binascii",
                "binhex",
                "bisect",
                "builtins",
                "bz2",
                "calendar",
                "cgi",
                "cgitb",
                "chunk",
                "cmath",
                "cmd",
                "code",
                "codecs",
                "codeop",
                "collections",
                "colorsys",
                "compileall",
                "concurrent",
                "configparser",
                "contextlib",
                "contextvars",
                "copy",
                "copyreg",
                "crypt",
                "csv",
                "ctypes",
                "curses",
                "dataclasses",
                "datetime",
                "dbm",
                "decimal",
                "difflib",
                "dis",
                "distutils",
                "doctest",
                "email",
                "encodings",
                "enum",
                "errno",
                "faulthandler",
                "fcntl",
                "filecmp",
                "fileinput",
                "fnmatch",
                "fractions",
                "ftplib",
                "functools",
                "gc",
                "getopt",
                "getpass",
                "gettext",
                "glob",
                "graphlib",
                "grp",
                "gzip",
                "hashlib",
                "heapq",
                "hmac",
                "html",
                "http",
                "imaplib",
                "imghdr",
                "imp",
                "importlib",
                "inspect",
                "io",
                "ipaddress",
                "itertools",
                "json",
                "keyword",
                "lib2to3",
                "linecache",
                "locale",
                "logging",
                "lzma",
                "mailbox",
                "mailcap",
                "marshal",
                "math",
                "mimetypes",
                "mmap",
                "modulefinder",
                "multiprocessing",
                "netrc",
                "nis",
                "nntplib",
                "numbers",
                "operator",
                "optparse",
                "os",
                "ossaudiodev",
                "pathlib",
                "pdb",
                "pickle",
                "pickletools",
                "pipes",
                "pkgutil",
                "platform",
                "plistlib",
                "poplib",
                "posix",
                "posixpath",
                "pprint",
                "profile",
                "pstats",
                "pty",
                "pwd",
                "py_compile",
                "pyclbr",
                "pydoc",
                "queue",
                "quopri",
                "random",
                "re",
                "readline",
                "reprlib",
                "resource",
                "rlcompleter",
                "runpy",
                "sched",
                "secrets",
                "select",
                "selectors",
                "shelve",
                "shlex",
                "shutil",
                "signal",
                "site",
                "smtpd",
                "smtplib",
                "sndhdr",
                "socket",
                "socketserver",
                "spwd",
                "sqlite3",
                "ssl",
                "stat",
                "statistics",
                "string",
                "stringprep",
                "struct",
                "subprocess",
                "sunau",
                "symtable",
                "sys",
                "sysconfig",
                "syslog",
                "tabnanny",
                "tarfile",
                "telnetlib",
                "tempfile",
                "termios",
                "test",
                "textwrap",
                "threading",
                "time",
                "timeit",
                "tkinter",
                "token",
                "tokenize",
                "tomllib",
                "trace",
                "traceback",
                "tracemalloc",
                "tty",
                "turtle",
                "turtledemo",
                "types",
                "typing",
                "unicodedata",
                "unittest",
                "urllib",
                "uu",
                "uuid",
                "venv",
                "warnings",
                "wave",
                "weakref",
                "webbrowser",
                "winreg",
                "winsound",
                "wsgiref",
                "xdrlib",
                "xml",
                "xmlrpc",
                "zipapp",
                "zipfile",
                "zipimport",
                "zlib",
                "_thread",
            }

    def add_entry_point(self, file_path: str):
        """
        Add a Python file as an entry point for dependency discovery.

        :param file_path: Absolute path to a Python file
        """
        if not os.path.exists(file_path):
            if self.verbose:
                print(f"Warning: Entry point does not exist: {file_path}")
            return

        if self.verbose:
            print(f"Added entry point: {file_path}")
        self.to_process.append(file_path)

    def _is_stdlib_module(self, module_name: str) -> bool:
        """
        Check if a module is part of the Python standard library.

        :param module_name: The module name to check
        :return: True if the module is from stdlib
        """
        # Check the root module name (e.g., 'os.path' -> 'os')
        root_module = module_name.split(".")[0]
        return root_module in self.stdlib_modules

    def _get_installed_packages(self) -> dict[str, str]:
        """
        Get all installed packages using pip's internal API or importlib.metadata.

        :return: Dictionary mapping package names to their locations
        """
        packages = {}

        # Try using importlib.metadata (Python 3.8+)
        try:
            if sys.version_info >= (3, 8):
                import importlib.metadata as metadata
            else:
                import importlib_metadata as metadata  # type: ignore

            distributions = metadata.distributions()
            for dist in distributions:
                name = dist.metadata["Name"]
                # Normalize package name (replace hyphens with underscores)
                normalized_name = name.replace("-", "_").lower()

                # Try to find the package location
                try:
                    # Get top-level modules/packages provided by this distribution
                    if dist.files:
                        # Find __init__.py or first .py file to get package location
                        for file in dist.files:
                            if file.suffix == ".py":
                                file_path = dist.locate_file(file)
                                if file_path.exists():
                                    # Get the site-packages directory
                                    site_packages = str(file_path).split(normalized_name)[0]
                                    pkg_path = os.path.join(site_packages, normalized_name)

                                    # Check if it's a package (directory) or module (file)
                                    if os.path.isdir(pkg_path):
                                        init_file = os.path.join(pkg_path, "__init__.py")
                                        if os.path.exists(init_file):
                                            packages[normalized_name] = init_file
                                            break
                                    elif os.path.isfile(pkg_path + ".py"):
                                        packages[normalized_name] = pkg_path + ".py"
                                        break

                    # Fallback: try importlib.util.find_spec
                    if normalized_name not in packages:
                        spec = importlib.util.find_spec(normalized_name)
                        if spec and spec.origin and spec.origin not in ("built-in", "frozen"):
                            packages[normalized_name] = spec.origin

                except Exception:
                    # If we can't resolve, try with the original name
                    try:
                        spec = importlib.util.find_spec(name.lower())
                        if spec and spec.origin and spec.origin not in ("built-in", "frozen"):
                            packages[name.lower()] = spec.origin
                    except Exception:
                        pass

            if self.verbose:
                print(f"Discovered {len(packages)} packages using importlib.metadata")
            return packages

        except ImportError:
            # importlib.metadata not available, fall back to subprocess
            pass

        # Fallback to subprocess if importlib.metadata is not available
        if self.verbose:
            print("importlib.metadata not available, trying subprocess...")

        # Try uv first (faster and more modern)
        try:
            result = subprocess.run(
                ["uv", "pip", "list", "--format", "json"], capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                package_list = json.loads(result.stdout)
                for pkg in package_list:
                    name = pkg["name"].replace("-", "_").lower()
                    # Try to resolve the package location
                    try:
                        spec = importlib.util.find_spec(name)
                        if spec and spec.origin and spec.origin not in ("built-in", "frozen"):
                            packages[name] = spec.origin
                    except Exception:
                        pass

                if self.verbose:
                    print(f"Discovered {len(packages)} packages using uv")
                return packages
        except (subprocess.TimeoutExpired, FileNotFoundError, json.JSONDecodeError):
            pass

        # Fallback to pip subprocess
        try:
            result = subprocess.run(["pip", "list", "--format", "json"], capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                package_list = json.loads(result.stdout)
                for pkg in package_list:
                    name = pkg["name"].replace("-", "_").lower()
                    try:
                        spec = importlib.util.find_spec(name)
                        if spec and spec.origin and spec.origin not in ("built-in", "frozen"):
                            packages[name] = spec.origin
                    except Exception:
                        pass

                if self.verbose:
                    print(f"Discovered {len(packages)} packages using pip")
                return packages
        except (subprocess.TimeoutExpired, FileNotFoundError, json.JSONDecodeError):
            pass

        if self.verbose:
            print("Warning: Could not discover packages using any method")
        return packages

    def _resolve_module(self, module_name: str) -> str | None:
        """
        Resolve a module name to its file path.

        :param module_name: The fully qualified module name
        :return: The file path of the module, or None if not found
        """
        try:
            spec = importlib.util.find_spec(module_name)
            if spec is None or spec.origin is None:
                return None

            # Skip built-in and frozen modules
            if spec.origin in ("built-in", "frozen"):
                return None

            return spec.origin
        except (ImportError, ModuleNotFoundError, ValueError, AttributeError):
            return None

    def _extract_imports(self, file_path: str) -> list[str]:
        """
        Extract all import statements from a Python file.

        :param file_path: Path to the Python file
        :return: List of imported module names
        """
        imports = []

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                source = f.read()

            tree = ast.parse(source, file_path)

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.append(node.module)
                        # Note: We only import the module itself.
                        # Imported names (functions, classes) within that module
                        # are not separate modules and don't need to be resolved.

        except (SyntaxError, UnicodeDecodeError) as e:
            if self.verbose:
                print(f"Error parsing {file_path}: {e}")
        return imports

    def _copy_module(self, module_name: str, module_path: str, target_dir: str):
        """
        Copy a module to the target directory, preserving package structure.

        :param module_name: The module's fully qualified name
        :param module_path: The source file path of the module
        :param target_dir: The target directory to copy to
        """
        # Determine if this is a package or a single module
        if module_path.endswith("__init__.py"):
            # This is a package, copy the entire package directory
            package_dir = os.path.dirname(module_path)

            # Get the package name from the module name
            # For 'foo.bar.baz', we want to determine which part is the root package
            parts = module_name.split(".")

            # Find the root package directory by going up the directory tree
            # until we find a directory without __init__.py in its parent
            current_dir = package_dir
            root_package_dir = package_dir

            # Go up to find the root package
            while True:
                parent_dir = os.path.dirname(current_dir)
                parent_init = os.path.join(parent_dir, "__init__.py")
                if os.path.exists(parent_init):
                    root_package_dir = parent_dir
                    current_dir = parent_dir
                else:
                    break

            # Get the root package name
            root_package_name = os.path.basename(root_package_dir)
            target_package_dir = os.path.join(target_dir, root_package_name)

            if os.path.exists(target_package_dir):
                if self.verbose:
                    print(f"Package already exists: {target_package_dir}")
                return

            if self.verbose:
                print(f"Copying package {root_package_name}: {root_package_dir} -> {target_package_dir}")

            shutil.copytree(root_package_dir, target_package_dir)
        else:
            # Single module file - need to handle nested package structure
            parts = module_name.split(".")

            if len(parts) > 1:
                # This module is inside a package, need to preserve structure
                # Find the root package directory by walking up from module_path
                module_dir = os.path.dirname(module_path)

                # Go up the directory tree to find the root package
                current_dir = module_dir
                root_package_dir = None

                # Walk up while we find __init__.py files
                while True:
                    init_file = os.path.join(current_dir, "__init__.py")
                    if os.path.exists(init_file):
                        root_package_dir = current_dir
                        parent_dir = os.path.dirname(current_dir)

                        # Check if parent also has __init__.py
                        parent_init = os.path.join(parent_dir, "__init__.py")
                        if os.path.exists(parent_init):
                            current_dir = parent_dir
                        else:
                            break
                    else:
                        break

                if root_package_dir:
                    root_package_name = os.path.basename(root_package_dir)
                    target_package_dir = os.path.join(target_dir, root_package_name)

                    if not os.path.exists(target_package_dir):
                        if self.verbose:
                            print(f"Copying package (from module): {root_package_dir} -> {target_package_dir}")
                        shutil.copytree(root_package_dir, target_package_dir)
                    else:
                        if self.verbose:
                            print(f"Package already exists: {target_package_dir}")
                else:
                    # Just copy the module file
                    module_filename = os.path.basename(module_path)
                    target_path = os.path.join(target_dir, module_filename)

                    if not os.path.exists(target_path):
                        if self.verbose:
                            print(f"Copying module {module_name}: {module_path} -> {target_path}")
                        shutil.copy2(module_path, target_path)
            else:
                # Top-level module file
                module_filename = os.path.basename(module_path)
                target_path = os.path.join(target_dir, module_filename)

                if os.path.exists(target_path):
                    if self.verbose:
                        print(f"Module already exists: {target_path}")
                    return

                if self.verbose:
                    print(f"Copying module {module_name}: {module_path} -> {target_path}")

                shutil.copy2(module_path, target_path)

    def collect(self, target_dir: str):
        """
        Collect and vendor all reachable dependencies to the target directory.

        :param target_dir: The directory to copy dependency modules into
        """
        if self.verbose:
            print(f"Starting dependency collection, target directory: {target_dir}")

        if self.use_package_manager:
            # Use package manager to get all installed packages
            if self.verbose:
                print("Using package manager to discover dependencies...")

            installed_packages = self._get_installed_packages()

            # Parse entry points to find which packages are imported
            # Then recursively check those packages for more imports
            imported_packages = set()
            to_check = deque()

            # Add entry points to check queue
            for entry_point in self.to_process:
                to_check.append(entry_point)

            checked_files = set()
            while to_check:
                current_file = to_check.popleft()

                if current_file in checked_files:
                    continue
                checked_files.add(current_file)

                try:
                    imports = self._extract_imports(current_file)
                    for imp in imports:
                        root_module = imp.split(".")[0]
                        # Skip stdlib and excluded packages
                        if self._is_stdlib_module(root_module):
                            continue
                        if root_module in self.excluded_packages:
                            continue

                        if root_module not in imported_packages:
                            imported_packages.add(root_module)
                            # If this package is installed, add ALL its Python files to check queue
                            # But skip if it's an excluded package
                            if root_module in installed_packages and root_module not in self.excluded_packages:
                                pkg_path = installed_packages[root_module]
                                pkg_dir = os.path.dirname(pkg_path)
                                # Walk the package directory to find all Python files
                                for root, _, files in os.walk(pkg_dir):
                                    # Skip directories of excluded packages
                                    skip_dir = False
                                    for excl in self.excluded_packages:
                                        if excl in root:
                                            skip_dir = True
                                            break
                                    if skip_dir:
                                        continue

                                    for file in files:
                                        if file.endswith(".py"):
                                            full_path = os.path.join(root, file)
                                            if full_path not in checked_files:
                                                # Skip if the file is in an excluded package directory
                                                skip_file = False
                                                for excl in self.excluded_packages:
                                                    if (
                                                        os.path.sep + excl + os.path.sep in full_path
                                                        or full_path.endswith(os.path.sep + excl)
                                                    ):
                                                        skip_file = True
                                                        break
                                                if not skip_file:
                                                    to_check.append(full_path)
                except Exception as e:
                    if self.verbose:
                        print(f"  Error parsing {current_file}: {e}")

            if self.verbose:
                print(f"Found {len(imported_packages)} imported packages: {sorted(imported_packages)}")

            # Add all installed packages that are imported
            for pkg_name, pkg_path in installed_packages.items():
                root_pkg = pkg_name.split(".")[0]
                # Skip if not imported or if it's an excluded package
                if root_pkg not in imported_packages:
                    continue
                if root_pkg in self.excluded_packages or pkg_name in self.excluded_packages:
                    if self.verbose:
                        print(f"  Skipping excluded package: {pkg_name}")
                    continue

                self.module_paths[pkg_name] = pkg_path
                if self.verbose:
                    print(f"  Including package: {pkg_name}")
        else:
            # Original AST-based recursive discovery
            # Process all entry points and their transitive dependencies
            while self.to_process:
                current_file = self.to_process.popleft()

                if current_file in self.visited_modules:
                    continue

                self.visited_modules.add(current_file)

                if self.verbose:
                    print(f"Processing: {current_file}")

                # Extract imports from this file
                imports = self._extract_imports(current_file)

                for module_name in imports:
                    # Skip if already processed
                    if module_name in self.module_paths:
                        continue

                    # Skip standard library modules
                    if self._is_stdlib_module(module_name):
                        if self.verbose:
                            print(f"  Skipping stdlib module: {module_name}")
                        continue

                    # Try to resolve the module
                module_path = self._resolve_module(module_name)

                if module_path is None:
                    if self.verbose:
                        print(f"  Could not resolve: {module_name}")
                    continue

                # Skip if the module is in the target directory (already vendored or part of project)
                # but exclude common virtual environment directories
                try:
                    # Check if module_path is within target_dir by comparing absolute paths
                    abs_module_path = os.path.abspath(module_path)
                    abs_target_dir = os.path.abspath(target_dir)

                    # Check if module is inside target_dir
                    if abs_module_path.startswith(abs_target_dir + os.sep):
                        # Get the relative path from target_dir
                        rel_path = os.path.relpath(abs_module_path, abs_target_dir)

                        # Check if it's in a virtual environment or cache directory
                        # These should NOT be considered project modules
                        venv_dirs = {
                            ".venv",
                            "venv",
                            "__pycache__",
                            ".tox",
                            ".nox",
                            "site-packages",
                            "dist-packages",
                            ".eggs",
                        }
                        first_component = rel_path.split(os.sep)[0]

                        # If the first directory component is NOT a venv/cache dir,
                        # then it's a project module
                        if first_component not in venv_dirs:
                            if self.verbose:
                                print(f"  Skipping project module: {module_name}")
                            continue
                except ValueError:
                    # Paths are on different drives or one is relative
                    pass

                if self.verbose:
                    print(f"  Found external dependency: {module_name} -> {module_path}")
                # Record this module
                self.module_paths[module_name] = module_path

                # Add to processing queue for transitive dependencies
                self.to_process.append(module_path)

        # Now copy all collected modules to the target directory
        if self.verbose:
            print(f"\nCopying {len(self.module_paths)} external modules to {target_dir}")

        for module_name, module_path in self.module_paths.items():
            try:
                self._copy_module(module_name, module_path, target_dir)
            except Exception as e:
                if self.verbose:
                    print(f"Error copying {module_name}: {e}")

        if self.verbose:
            print("Dependency collection complete")
