# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x((31, 14, 30))
b = x(43)
