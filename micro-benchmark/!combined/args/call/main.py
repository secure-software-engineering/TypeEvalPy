# A function func is defined which takes as a parameter a function which it later calls.
# The 'param_func' function returns a string value.
def param_func():
    return "Hello from param_func"

def func(a):
    return a()

b = func(param_func)
 