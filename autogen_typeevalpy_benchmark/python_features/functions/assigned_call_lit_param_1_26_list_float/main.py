# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x([35, 88, 11])
b = x(18.85)
