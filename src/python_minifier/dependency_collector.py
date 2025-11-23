"""
Dependency collector for tree shaking and vendoring external dependencies.
"""

import ast
import importlib
import importlib.util
import os
import shutil
import sys
from typing import Set


class DependencyCollector:
    """
    Collects and vendors external dependencies used by a Python project.
    
    Performs tree shaking by only including modules that are reachable
    (directly or indirectly) from the project code.
    """
    
    def __init__(self, verbose: bool = False):
        """
        Initialize the dependency collector.
        
        :param verbose: If True, print debug information during collection
        """
        self.verbose = verbose
        self.visited_modules: Set[str] = set()
        self.to_process: list[str] = []
        self.module_paths: dict[str, str] = {}  # module_name -> file_path
        
        # Use sys.stdlib_module_names for Python 3.10+ (recommended: Python 3.12+)
        # For older Python versions, basic stdlib detection via importlib will still work
        if hasattr(sys, 'stdlib_module_names'):
            self.stdlib_modules = sys.stdlib_module_names
        else:
            # Minimal fallback for common stdlib modules on older Python
            # Note: This is not comprehensive. Consider upgrading to Python 3.10+
            self.stdlib_modules = {
                'abc', 'aifc', 'argparse', 'array', 'ast', 'asynchat', 'asyncio', 'asyncore', 
                'atexit', 'audioop', 'base64', 'bdb', 'binascii', 'binhex', 'bisect', 'builtins',
                'bz2', 'calendar', 'cgi', 'cgitb', 'chunk', 'cmath', 'cmd', 'code', 'codecs',
                'codeop', 'collections', 'colorsys', 'compileall', 'concurrent', 'configparser',
                'contextlib', 'contextvars', 'copy', 'copyreg', 'crypt', 'csv', 'ctypes', 'curses',
                'dataclasses', 'datetime', 'dbm', 'decimal', 'difflib', 'dis', 'distutils', 'doctest',
                'email', 'encodings', 'enum', 'errno', 'faulthandler', 'fcntl', 'filecmp', 'fileinput',
                'fnmatch', 'fractions', 'ftplib', 'functools', 'gc', 'getopt', 'getpass', 'gettext',
                'glob', 'graphlib', 'grp', 'gzip', 'hashlib', 'heapq', 'hmac', 'html', 'http', 'imaplib',
                'imghdr', 'imp', 'importlib', 'inspect', 'io', 'ipaddress', 'itertools', 'json', 'keyword',
                'lib2to3', 'linecache', 'locale', 'logging', 'lzma', 'mailbox', 'mailcap', 'marshal',
                'math', 'mimetypes', 'mmap', 'modulefinder', 'multiprocessing', 'netrc', 'nis', 'nntplib',
                'numbers', 'operator', 'optparse', 'os', 'ossaudiodev', 'pathlib', 'pdb', 'pickle',
                'pickletools', 'pipes', 'pkgutil', 'platform', 'plistlib', 'poplib', 'posix', 'posixpath',
                'pprint', 'profile', 'pstats', 'pty', 'pwd', 'py_compile', 'pyclbr', 'pydoc', 'queue',
                'quopri', 'random', 're', 'readline', 'reprlib', 'resource', 'rlcompleter', 'runpy',
                'sched', 'secrets', 'select', 'selectors', 'shelve', 'shlex', 'shutil', 'signal',
                'site', 'smtpd', 'smtplib', 'sndhdr', 'socket', 'socketserver', 'spwd', 'sqlite3',
                'ssl', 'stat', 'statistics', 'string', 'stringprep', 'struct', 'subprocess', 'sunau',
                'symtable', 'sys', 'sysconfig', 'syslog', 'tabnanny', 'tarfile', 'telnetlib', 'tempfile',
                'termios', 'test', 'textwrap', 'threading', 'time', 'timeit', 'tkinter', 'token',
                'tokenize', 'tomllib', 'trace', 'traceback', 'tracemalloc', 'tty', 'turtle', 'turtledemo',
                'types', 'typing', 'typing_extensions', 'unicodedata', 'unittest', 'urllib', 'uu', 'uuid',
                'venv', 'warnings', 'wave', 'weakref', 'webbrowser', 'winreg', 'winsound', 'wsgiref',
                'xdrlib', 'xml', 'xmlrpc', 'zipapp', 'zipfile', 'zipimport', 'zlib', '_thread'
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
        root_module = module_name.split('.')[0]
        return root_module in self.stdlib_modules
        
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
            if spec.origin in ('built-in', 'frozen'):
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
            with open(file_path, 'r', encoding='utf-8') as f:
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
        if module_path.endswith('__init__.py'):
            # This is a package, copy the entire package directory
            package_dir = os.path.dirname(module_path)
            
            # Get the package name from the module name
            # For 'foo.bar.baz', we want to determine which part is the root package
            parts = module_name.split('.')
            
            # Find the root package directory by going up the directory tree
            # until we find a directory without __init__.py in its parent
            current_dir = package_dir
            root_package_dir = package_dir
            
            # Go up to find the root package
            while True:
                parent_dir = os.path.dirname(current_dir)
                parent_init = os.path.join(parent_dir, '__init__.py')
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
            parts = module_name.split('.')
            
            if len(parts) > 1:
                # This module is inside a package, need to preserve structure
                # Find the root package directory by walking up from module_path
                module_dir = os.path.dirname(module_path)
                
                # Go up the directory tree to find the root package
                current_dir = module_dir
                root_package_dir = None
                
                # Walk up while we find __init__.py files
                while True:
                    init_file = os.path.join(current_dir, '__init__.py')
                    if os.path.exists(init_file):
                        root_package_dir = current_dir
                        parent_dir = os.path.dirname(current_dir)
                        
                        # Check if parent also has __init__.py
                        parent_init = os.path.join(parent_dir, '__init__.py')
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
            
        # Process all entry points and their transitive dependencies
        while self.to_process:
            current_file = self.to_process.pop(0)
            
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
                try:
                    # Check if module_path is within target_dir
                    abs_module_path = os.path.abspath(module_path)
                    abs_target_dir = os.path.abspath(target_dir)
                    common = os.path.commonpath([abs_module_path, abs_target_dir])
                    if common == abs_target_dir:
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
