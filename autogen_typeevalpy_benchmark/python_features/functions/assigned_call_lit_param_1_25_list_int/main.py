# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x([59, 21, 91])
b = x(73)
