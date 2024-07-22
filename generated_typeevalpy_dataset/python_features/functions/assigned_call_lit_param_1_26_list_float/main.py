# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x([52, 70, 77])
b = x(74.55)
