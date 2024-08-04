# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x((71, 60, 8))
b = x(False)
