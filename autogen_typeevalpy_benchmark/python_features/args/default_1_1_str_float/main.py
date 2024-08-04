# A function func is defined which takes as a parameter a function which it later calls. It also has a default value assigned
# The 'param_func' function returns a string value.
# The 'param_func2' function returns an integer value.
def param_func():
    return 'bqngm'


def param_func2():
    return 27.72


def func(a=param_func2):
    return a()


b = func(param_func)
c = func()
