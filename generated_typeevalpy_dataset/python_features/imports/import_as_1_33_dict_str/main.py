# The `main` module imports `to_import` as `as_import_name`. `to_import` defines a function.


import to_import as as_to_import


def func():
    return {'gohuh': 41, 'ezzjc': 96, 'lgplh': 92}


a = func()
b = as_to_import.func()
