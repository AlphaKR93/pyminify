import os
import sys
import python_minifier.ast as ast

from dataclasses import dataclass
from typing import NamedTuple

from python_minifier.rename import add_namespace, bind_names, resolve_names, rename_literals
from python_minifier.rename.renamer import NameAssigner, add_assigned, name_filter
from python_minifier.printer import ModulePrinter
from python_minifier.transforms.remove_environment_checks import RemoveEnvironmentChecks
from python_minifier.transforms.combine_imports import CombineImports
from python_minifier.transforms.remove_annotations import RemoveAnnotations
from python_minifier.transforms.remove_annotations_options import RemoveAnnotationsOptions
from python_minifier.transforms.remove_pass import RemovePass
from python_minifier.transforms.remove_literal_statements import RemoveLiteralStatements
from python_minifier.transforms.remove_posargs import remove_posargs
from python_minifier.transforms.remove_object_base import RemoveObject
from python_minifier.transforms.remove_asserts import RemoveAsserts
from python_minifier.transforms.remove_debug import RemoveDebug
from python_minifier.transforms.remove_explicit_return_none import RemoveExplicitReturnNone
from python_minifier.transforms.constant_folding import FoldConstants
from python_minifier.transforms.remove_exception_brackets import remove_no_arg_exception_call
from python_minifier.transforms.remove_unused_imports import remove_unused_imports


@dataclass(frozen = True)
class PackageMinifyOptions:
    package_path: str
    remove_annotations: RemoveAnnotationsOptions = RemoveAnnotationsOptions()
    remove_pass: bool = True
    remove_literal_statements: bool = True
    combine_imports: bool = True
    hoist_literals: bool = True
    mangle: bool = False
    preserved_names: frozenset[str] = frozenset({})
    remove_unused_imports: bool = True
    preserved_imports: frozenset[str] = frozenset({})
    remove_object_base: bool = True
    convert_posargs_to_args: bool = True
    preserve_shebang: bool = False
    remove_asserts: bool = False
    remove_debug: bool = False
    remove_environment_checks: bool = True
    remove_explicit_return_none: bool = True
    remove_builtin_exception_brackets: bool = True
    constant_folding: bool = True
    allow_utf8_names: bool = True

class AbstractModule(NamedTuple):
    package: str
    module: ast.Module

_EMPTY = AbstractModule('', None)  # pyright: ignore[reportArgumentType]

class ProjectMinifier:
    root_path: str
    packages: dict[PackageMinifyOptions, dict[str, ast.Module]] # path -> PackageMinifyOptions
    modules: dict[str, AbstractModule] = {} # dotted.name -> ast.Module

    def __init__(
        self,
        root_path: str,
        /,
        *packages: PackageMinifyOptions,
        python_version: tuple[int, int, int, str, int] = sys.version_info,
        verbose: bool = False
    ):
        self.python_version = python_version
        self.verbose = verbose
        self.root_path = root_path
        self.packages = {PackageMinifyOptions(**(package.__dict__ | {"package_path": os.path.abspath(package.package_path)})): {} for package in packages}

    def _load_module(self, package: PackageMinifyOptions, root: str, file: str):
        full_path = os.path.join(root, file)
        rel_path = os.path.relpath(full_path, self.root_path)

        module_name = rel_path.replace(os.path.sep, '.')[:-3]
        is_package = False

        if file == '__init__.py':
            module_name = os.path.dirname(rel_path).replace(os.path.sep, '.')
            if module_name == '.':
                module_name = ''
            is_package = True

        if module_name == '.':
            return

        with open(full_path, 'r', encoding='utf-8') as f:
            source = f.read().replace("#if !__debug__:", "")

        try:
            tree = ast.parse(source, full_path)
        except SyntaxError as e:
            print(f"Error parsing {full_path}: {e}")
            return

        ast.add_parent(tree)
        add_namespace(tree)

        if package.combine_imports:
            tree = CombineImports()(tree)

        bind_names(tree)
        resolve_names(tree)

        self.packages[package][full_path] = tree
        
        if module_name:
            self.modules[module_name] = AbstractModule(
                module_name if is_package else '.'.join(module_name.split('.')[:-1]),
                tree
            )

        if self.verbose:
            print("Loaded module", full_path)

    def load_project(self):
        for package in self.packages.keys():
            for root, _, files in os.walk(package.package_path):
                for file in files:
                    if file.endswith('.py'):
                        self._load_module(package, root, file)

    def resolve_relative_import(self, current_module_name, level, module_part):
        current_pkg = self.modules.get(current_module_name, _EMPTY).package
        pkg_parts = current_pkg.split('.') if current_pkg else []
        
        if level > 0:
            pop_count = level - 1
            if pop_count > len(pkg_parts):
                return None
            
            if pop_count > 0:
                target_pkg_parts = pkg_parts[:-pop_count]
            else:
                target_pkg_parts = pkg_parts
            
            target_pkg = '.'.join(target_pkg_parts)
            
            if module_part:
                return f"{target_pkg}.{module_part}" if target_pkg else module_part
            else:
                return target_pkg
        return None

    def _get_module_preserved_names(self, preserved_options: frozenset[str], current_module_name: str | None) -> set[str]:
        """
        Parse preserved options and return the set of names to preserve for the current module.
        Supports 'name' (global) and 'module.path:name' (scoped) formats.
        """
        preserved_names = set()
        
        for p in preserved_options:
            if ':' in p:
                # Scoped preservation: module.name:variable
                mod_part, name_part = p.split(':', 1)
                if current_module_name == mod_part:
                    preserved_names.add(name_part)
            else:
                # Global preservation
                preserved_names.add(p)
        
        return preserved_names

    def resolve_cross_module_references(self):
        print("Resolving cross-module references...")
        
        path_to_name = {v.module: k for k, v in self.modules.items()}

        for project, modules in self.packages.items():
            for path, module in modules.items():
                current_module_name = path_to_name.get(module)
                # [Modified] Apply preserved names based on module scope
                preserved_for_module = self._get_module_preserved_names(project.preserved_names, current_module_name)
                
                for binding in module.bindings:
                    if binding.name in preserved_for_module:
                        # Mark for export instead of disallowing rename
                        binding.export_as = binding.name

        for project, modules in self.packages.items():
            for path, module in modules.items():
                current_module_name = path_to_name.get(module)
                bindings_to_remove = []

                for binding in module.bindings:
                    # ... (existing logic for cross-reference resolution)
                    import_node = None
                    alias_node = None

                    for ref in binding.references:
                        if isinstance(ref, ast.alias):
                            alias_node = ref
                            parent = ref
                            while hasattr(parent, '_parent'):
                                parent = parent._parent
                                if isinstance(parent, ast.ImportFrom):
                                    import_node = parent
                                    break
                            if import_node:
                                break

                    if import_node:
                        target_module_name = None
                        if import_node.level > 0:
                            target_module_name = self.resolve_relative_import(
                                current_module_name,
                                import_node.level,
                                import_node.module
                            )
                        else:
                            target_module_name = import_node.module

                        if target_module_name:
                            target_module = self.modules.get(target_module_name)

                            if target_module:
                                imported_name = alias_node.name
                                target_binding = None

                                for b in target_module.module.bindings:
                                    if b.name == imported_name:
                                        target_binding = b
                                        break

                                if target_binding:
                                    if target_binding is binding:
                                        continue

                                    if self.verbose:
                                        print(f"Linked {path}: {binding.name} -> {target_module_name}.{target_binding.name}")

                                    # [Modified] Check preservation using scoped logic for the target module?
                                    # The target binding's disallow_rename is already handled in the first loop above based on its own module name.
                                    # Here we just propagate the disallow_rename if the local alias is preserved/disallowed.
                                    
                                    # Note: project.preserved check here strictly needs to check if THIS binding (in current module) is preserved.
                                    current_module_preserved = self._get_module_preserved_names(project.preserved_names, current_module_name)
                                    
                                    if not binding.allow_rename or binding.name in current_module_preserved:
                                        target_binding.disallow_rename()

                                    alias_node._is_project_reference = True

                                    for ref_node in list(binding.references):
                                        target_binding.add_reference(ref_node)

                                    bindings_to_remove.append(binding)

                for b in bindings_to_remove:
                    module.bindings.remove(b)

    def minify(self):
        self.load_project()
        self.resolve_cross_module_references()

        for package, modules in self.packages.items():
            if package.remove_literal_statements:
                for path, module in modules.items():
                    modules[path] = RemoveLiteralStatements()(module)

        for package, modules in self.packages.items():
            if package.remove_annotations:
                for path, module in modules.items():
                    modules[path] = RemoveAnnotations(package.remove_annotations)(module)

        for package, modules in self.packages.items():
            if package.remove_object_base:
                for path, module in modules.items():
                    modules[path] = RemoveObject()(module)

        for package, modules in self.packages.items():
            if package.remove_explicit_return_none:
                for path, module in modules.items():
                    modules[path] = RemoveExplicitReturnNone()(module)

        for package, modules in self.packages.items():
            if package.constant_folding:
                for path, module in modules.items():
                    modules[path] = FoldConstants()(module)

        for package, modules in self.packages.items():
            if package.remove_builtin_exception_brackets:
                for path, module in modules.items():
                    if not module.tainted:
                        remove_no_arg_exception_call(module)

        for package, modules in self.packages.items():
            if package.remove_unused_imports:
                for path, module in modules.items():
                    if not path.endswith("__init__.py"):
                        module = remove_unused_imports(module, package.preserved_imports)

        for package, modules in self.packages.items():
            if package.hoist_literals:
                for path, module in modules.items():
                    rename_literals(module)

        for package, modules in self.packages.items():
            for path, module in modules.items():
                add_assigned(module)

        # Prepare map for name resolution (module object -> dotted name)
        # We need this because 'modules' dict here is path->module, but we track names by dotted name in self.modules
        path_to_name = {v.module: k for k, v in self.modules.items()}

        for package, modules in self.packages.items():
            assigner = NameAssigner(name_generator=name_filter(allow_unicode=package.allow_utf8_names))
            if package.mangle:
                for path, module in modules.items():
                    # [Modified] Calculate preserved names for this specific module
                    current_module_name = path_to_name.get(module)
                    module_specific_preserved = self._get_module_preserved_names(package.preserved_names, current_module_name)
                    
                    assigner(module, prefix_globals=False, reserved_globals=module_specific_preserved)

        for package, modules in self.packages.items():
            for path, module in modules.items():
                if package.remove_asserts:
                    module = RemoveAsserts()(module)

                if package.remove_debug:
                    module = RemoveDebug()(module)
                    
                if package.remove_environment_checks:
                    module = RemoveEnvironmentChecks(self.python_version)(module)

                if package.convert_posargs_to_args:
                    module = remove_posargs(module)

                if package.remove_pass:
                    modules[path] = RemovePass()(module)

                modules[path] = module

        for package, modules in self.packages.items():
            for path, module in modules.items():
                minified_code = ModulePrinter()(module)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(minified_code)
                if self.verbose:
                    print(f"Minified: {path}")

    __call__ = minify
