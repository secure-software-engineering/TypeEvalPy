# The `main` module imports `nested.to_import` module and this module in turn imports `to_import2`

from nested import to_import


def func():
    return {'hidmh': 69, 'ldekn': 15, 'rczmn': 73}


a = func()
b = to_import.func()
c = to_import.to_import2.func()
