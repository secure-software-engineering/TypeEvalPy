def param_func():
    return "Hello from param_func"


def func(a):
    return a()


b = param_func
c = func(b)
