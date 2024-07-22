# The `main` module imports `to_import` as `as_import_name`. `to_import` defines a function.


import to_import as as_to_import


def func():
    return {'uarms': 74, 'npuus': 13, 'oksxt': 69}


a = func()
b = as_to_import.func()
