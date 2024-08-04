# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x((31, 94, 10))
b = x(75.0)
