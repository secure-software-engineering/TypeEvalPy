# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x((16, 45, 31))
b = x(82.76)
