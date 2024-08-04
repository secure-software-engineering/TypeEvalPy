# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x([21, 24, 76])
b = x(True)
