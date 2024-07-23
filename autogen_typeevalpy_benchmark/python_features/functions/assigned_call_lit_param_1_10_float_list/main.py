# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x(38.14)
b = x([26, 49, 42])
