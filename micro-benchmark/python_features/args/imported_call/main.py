# Imports a function from another module and calls it with another function.

from to_import_call import func


def param_func():
    return "Hello from param_func"


b = func(param_func)
