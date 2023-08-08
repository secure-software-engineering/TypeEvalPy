import os
import shutil


def delete_python_files_except_whitelist(directory, whitelist):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and str(os.path.join(root, file)) not in whitelist:
                try:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    shutil.rmtree(root)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    pass
            """elif file.endswith(".py"):
                file_path = os.path.join(root, file)
                print(f"|||||||||||||||||||||||| Not Deleted: {file_path}")"""


# Specify the directory to start the search from
starting_directory = "/tmp/micro-benchmark"

# List of Python files to retain
# for hityper
file_whitelist = [
    "/tmp/micro-benchmark/analysis_sensitivities/flow_sensitivity/arithmetic/arithmetic.py",
    "/tmp/micro-benchmark/analysis_sensitivities/flow_sensitivity/combined/combined_types.py",
    "/tmp/micro-benchmark/analysis_sensitivities/flow_sensitivity/identity/identity.py",
    "/tmp/micro-benchmark/analysis_sensitivities/intra_procedural/arithmetic/arithmetic.py",
    "/tmp/micro-benchmark/analysis_sensitivities/intra_procedural/combined/combined_types.py",
    "/tmp/micro-benchmark/python_features/assignments/generators/main.py",
    "/tmp/micro-benchmark/python_features/builtins/functions/main.py",
    "/tmp/micro-benchmark/python_features/builtins/itertools/main.py",
    "/tmp/micro-benchmark/python_features/builtins/types/main.py",
    "/tmp/micro-benchmark/python_features/builtins/zip/main.py",
    "/tmp/micro-benchmark/python_features/classes/imported_attr_access/main.py",
    "/tmp/micro-benchmark/python_features/classes/imported_call/main.py ",
    "/tmp/micro-benchmark/python_features/classes/imported_call_without_init/main.py",
    "/tmp/micro-benchmark/python_features/classes/imported_nested_attr_access/main.py",
    "/tmp/micro-benchmark/python_features/classes/imported_nested_attr_access/nest/__init__.py",
    "/tmp/micro-benchmark/python_features/dicts/ext_key/ext.py",
    "/tmp/micro-benchmark/python_features/dicts/merge/main.py",
    "/tmp/micro-benchmark/python_features/dicts/merge_pipe/main.py",
    "/tmp/micro-benchmark/python_features/dicts/zip/main.py",
    "/tmp/micro-benchmark/python_features/direct_calls/imported_return_call/main.py",
    "/tmp/micro-benchmark/python_features/direct_calls/lambda/main.py",
    "/tmp/micro-benchmark/python_features/dynamic/compile/main.py",
    "/tmp/micro-benchmark/python_features/dynamic/exec/main.py",
    "/tmp/micro-benchmark/python_features/external/attribute/main.py",
    "/tmp/micro-benchmark/python_features/external/function/main.py",
    "/tmp/micro-benchmark/python_features/external/function_asname/main.py",
    "/tmp/micro-benchmark/python_features/external/function_assigned/main.py ",
    "/tmp/micro-benchmark/python_features/external/typeevalpy_external_module/setup.py",
    "/tmp/micro-benchmark/python_features/external/typeevalpy_external_module/typeevalpy_external_module/__init__.py",
    "/tmp/micro-benchmark/python_features/external/typeevalpy_external_module/typeevalpy_external_module/ext.py",
    "/tmp/micro-benchmark/python_features/functions/imported_call/main.py",
    "/tmp/micro-benchmark/python_features/imports/chained_import/main.py",
    "/tmp/micro-benchmark/python_features/imports/import_all/main.py",
    "/tmp/micro-benchmark/python_features/imports/import_from/main.py",
    "/tmp/micro-benchmark/python_features/imports/init_func_import/main.py ",
    "/tmp/micro-benchmark/python_features/imports/init_import/main.py",
    "/tmp/micro-benchmark/python_features/imports/init_import/nested_init/__init__.py",
    "/tmp/micro-benchmark/python_features/imports/parent_import/__init__.py",
    "/tmp/micro-benchmark/python_features/imports/parent_import/nested/__init__.py",
    "/tmp/micro-benchmark/python_features/imports/relative_import/__init__.py",
    "/tmp/micro-benchmark/python_features/imports/relative_import/nested/__init__.py",
    "/tmp/micro-benchmark/python_features/imports/relative_import/nested/to_import.py",
    "/tmp/micro-benchmark/python_features/imports/relative_import_with_name/__init__.py",
    "/tmp/micro-benchmark/python_features/imports/relative_import_with_name/main.py",
    "/tmp/micro-benchmark/python_features/imports/relative_import_with_name/nested_rel/__init__.py",
    "/tmp/micro-benchmark/python_features/imports/simple_import/main.py",
    "/tmp/micro-benchmark/python_features/imports/submodule_import/main.py",
    "/tmp/micro-benchmark/python_features/imports/submodule_import_all/from_all/__init__.py",
    "/tmp/micro-benchmark/python_features/imports/submodule_import_all/main.py",
    "/tmp/micro-benchmark/python_features/imports/submodule_import_as/main.py",
    "/tmp/micro-benchmark/python_features/imports/submodule_import_from/from_module_sub/__init__.py",
    "/tmp/micro-benchmark/python_features/imports/submodule_import_from/main.py",
    "/tmp/micro-benchmark/python_features/lambdas/call/main.py",
    "/tmp/micro-benchmark/python_features/lambdas/composition/main.py",
    "/tmp/micro-benchmark/python_features/lists/copy/main.py",
    "/tmp/micro-benchmark/python_features/lists/ext_index/ext.py",
    "/tmp/micro-benchmark/python_features/lists/unpacking/main.py",
    "/tmp/micro-benchmark/python_features/returns/imported_call/main.py",
    "/tmp/micro-benchmark/python_features/returns/nested_import_call/main.py",
]

delete_python_files_except_whitelist(starting_directory, file_whitelist)
