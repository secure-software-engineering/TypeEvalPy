# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x(22.4)
b = x((34, 33, 79))
