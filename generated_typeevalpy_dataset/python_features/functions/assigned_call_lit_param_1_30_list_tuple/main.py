# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x([65, 6, 32])
b = x((45, 97, 78))
