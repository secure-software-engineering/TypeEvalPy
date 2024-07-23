# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x((23, 72, 59))
b = x([73, 44, 69])
