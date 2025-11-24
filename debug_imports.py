#!/usr/bin/env python
"""Debug script to understand why imports between vendored dependencies fail"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import debugpy

# Start debugpy server
debugpy.listen(("localhost", 5678))
print("Waiting for debugger to attach on localhost:5678...")
debugpy.wait_for_client()
print("Debugger attached!")

# Now run the build to debug
os.chdir('/tmp/test_build')

# Create a simple test case
os.makedirs('test_mod1', exist_ok=True)
os.makedirs('test_mod2', exist_ok=True)

# Create test_mod1/__init__.py with a class
with open('test_mod1/__init__.py', 'w') as f:
    f.write('class MyClass:\n    pass\n')

# Create test_mod2/use.py that imports from test_mod1
with open('test_mod2/__init__.py', 'w') as f:
    f.write('from test_mod1 import MyClass\n')

# Now minify with module obfuscation and mangling
from python_minifier.project_minifier import ProjectMinifier, PackageMinifyOptions

# Set breakpoint before minification
debugpy.breakpoint()

minifier = ProjectMinifier(
    ".",
    PackageMinifyOptions(
        package_path="test_mod1",
        mangle=True,
        obfuscate_module_names=True,
    ),
    PackageMinifyOptions(
        package_path="test_mod2",
        mangle=True,
        obfuscate_module_names=True,
    ),
    verbose=True
)

minifier.minify()

print("\n=== Minified files ===")
import glob
for f in glob.glob("**/*.py", recursive=True):
    print(f"\n{f}:")
    with open(f) as fh:
        print(fh.read())
