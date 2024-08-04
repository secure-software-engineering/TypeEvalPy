# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x([50, 19, 63])
b = x(88)
