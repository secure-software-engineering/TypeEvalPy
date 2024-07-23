# The `main` module imports `nested.to_import` module and this module in turn imports `to_import2`

from nested import to_import


def func():
    return {'dlpfj': 6, 'twzci': 82, 'gwwlr': 82}


a = func()
b = to_import.func()
c = to_import.to_import2.func()
