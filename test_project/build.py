#!/usr/bin/env python

from python_minifier.project_minifier import ProjectMinifier, PackageMinifyOptions
from python_minifier.transforms.remove_annotations_options import RemoveAnnotationsOptions

ProjectMinifier(
    ".",
    PackageMinifyOptions(
        package_path="app",
        remove_annotations=RemoveAnnotationsOptions(
            remove_variable_annotations=True,
            remove_return_annotations=True,
            remove_argument_annotations=False,
            remove_class_attribute_annotations=False,
            aggressively_minify_class_attributes=False,
        ),
        mangle=True,
        preserved_names=frozenset({"app.app:app",}),
        remove_asserts=True,
        remove_debug=True,
        obfuscate_module_names=True,
        vendor_dependencies=True,
    ),
    PackageMinifyOptions(
        package_path="lib",
        remove_annotations=RemoveAnnotationsOptions(
            remove_variable_annotations=True,
            remove_return_annotations=True,
            remove_argument_annotations=True,
            remove_class_attribute_annotations=True,
            aggressively_minify_class_attributes=False,
        ),
        mangle=True,
        preserved_imports=frozenset(),
        remove_asserts=True,
        remove_debug=True,
        obfuscate_module_names=True,
        vendor_dependencies=True,
    ),
    vendored_deps_options=PackageMinifyOptions(
        package_path="",  # Will be overridden
        remove_literal_statements=True,
        hoist_literals=True,
        mangle=True,
        remove_unused_imports=True,
        remove_environment_checks=True,
        constant_folding=True,
        remove_inline_functions=True,
        obfuscate_module_names=True,
    ),
    python_version=(3, 12),
)()
