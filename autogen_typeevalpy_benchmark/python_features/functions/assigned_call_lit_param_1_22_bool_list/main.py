# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x(False)
b = x([26, 70, 93])
