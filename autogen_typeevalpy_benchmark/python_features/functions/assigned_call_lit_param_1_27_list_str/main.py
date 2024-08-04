# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x([38, 6, 93])
b = x('rzhei')
