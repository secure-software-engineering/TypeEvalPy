# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x(17.73)
b = x((21, 97, 23))
