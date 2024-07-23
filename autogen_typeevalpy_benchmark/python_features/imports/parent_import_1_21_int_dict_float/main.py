# The `main` module imports `nested.to_import` module and this module in turn imports `to_import2`

from nested import to_import


def func():
    return {'akfjt': 11, 'wvoae': 27, 'wmwya': 12}


a = func()
b = to_import.func()
c = to_import.to_import2.func()
