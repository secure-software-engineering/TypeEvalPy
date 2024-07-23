# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x((40, 30, 76))
b = x(17.1)
