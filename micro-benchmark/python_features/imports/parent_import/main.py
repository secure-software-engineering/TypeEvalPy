# The `main` module imports `nested.to_import` module and this module in turn imports `to_import2` via the command `from .. import to_import2`


from nested import to_import


def func():
    return "Hello from main module"


a = func()
