# The `main` module imports `to_import` as `as_import_name`. `to_import` defines a function.


import to_import as as_to_import


def func():
    return {'brwus': 23, 'idjtx': 44, 'cdtlh': 68}


a = func()
b = as_to_import.func()
