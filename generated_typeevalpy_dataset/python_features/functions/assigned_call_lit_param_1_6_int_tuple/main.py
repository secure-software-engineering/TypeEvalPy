# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x(61)
b = x((91, 82, 18))
