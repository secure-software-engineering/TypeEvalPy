# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x((4, 80, 95))
b = x(47)
