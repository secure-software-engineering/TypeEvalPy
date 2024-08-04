# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x([46, 26, 44])
b = x((71, 94, 30))
