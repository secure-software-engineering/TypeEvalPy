# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x([4, 99, 75])
b = x(86.32)
