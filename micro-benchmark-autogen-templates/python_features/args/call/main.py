# A function func is defined which takes as a parameter a function which it later calls.
# The 'param_func' function returns a string value.
def param_func():
    return <value1>


def func(a):
    return a()


b = func(param_func)
