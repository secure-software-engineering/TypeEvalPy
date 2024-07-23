# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x((19, 52, 71))
b = x(False)
