# The `main` module imports `to_import` as `as_import_name`. `to_import` defines a function.


import to_import as as_to_import


def func():
    return [29, 4, 17]


a = func()
b = as_to_import.func()
