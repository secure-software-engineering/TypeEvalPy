# The `main` module imports `to_import` module. `to_import` module defines a function which is called.


import to_import


def func():
    return "Hello from main module"


a = func()
