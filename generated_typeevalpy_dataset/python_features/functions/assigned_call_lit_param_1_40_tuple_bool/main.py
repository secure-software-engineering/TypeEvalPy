# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x((39, 1, 85))
b = x(True)
