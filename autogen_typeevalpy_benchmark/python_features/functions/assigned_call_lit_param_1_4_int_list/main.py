# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x(83)
b = x([51, 42, 69])
