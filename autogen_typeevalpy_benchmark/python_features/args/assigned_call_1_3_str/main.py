# A function object assigned to a variable and passed as an argument to another function.
# A function `func` is defined which takes as a parameter a variable which has a function 'param_func' assigned to it which it later calls.
# The 'param_func' function returns a string value.
def param_func():
    return 'mlczq'


def func(a):
    return a()


b = param_func
c = func(b)
