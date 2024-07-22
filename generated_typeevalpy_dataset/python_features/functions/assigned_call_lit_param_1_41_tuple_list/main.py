# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x((9, 73, 54))
b = x([62, 96, 66])
