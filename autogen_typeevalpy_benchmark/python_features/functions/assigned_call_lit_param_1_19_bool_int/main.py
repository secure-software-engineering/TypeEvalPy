# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x(True)
b = x(63)
