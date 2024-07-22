# The `main` module imports `nested.to_import` module and this module in turn imports `to_import2`

from nested import to_import


def func():
    return {'azbyp': 19, 'guomp': 51, 'zewdy': 63}


a = func()
b = to_import.func()
c = to_import.to_import2.func()
