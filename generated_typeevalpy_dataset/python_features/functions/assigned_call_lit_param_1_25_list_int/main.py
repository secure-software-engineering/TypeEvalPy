# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x([20, 49, 71])
b = x(84)
