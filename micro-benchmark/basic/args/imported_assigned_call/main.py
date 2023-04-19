#Import a function from another module and call it with a function parameter which as been assigned to a variable.

from to_import import func

def param_func():
    return "Hello from param_func"

a = param_func
b = func(a)
