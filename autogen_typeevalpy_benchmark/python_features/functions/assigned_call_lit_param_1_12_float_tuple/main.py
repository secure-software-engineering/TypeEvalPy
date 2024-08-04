# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x(70.54)
b = x((2, 4, 13))
