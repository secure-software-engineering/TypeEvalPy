# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x(95)
b = x((32, 49, 98))
