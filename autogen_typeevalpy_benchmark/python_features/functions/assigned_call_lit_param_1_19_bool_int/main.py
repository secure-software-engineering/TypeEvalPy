# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x(False)
b = x(36)
