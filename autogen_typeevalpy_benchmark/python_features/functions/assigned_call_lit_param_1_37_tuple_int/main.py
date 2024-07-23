# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x((63, 100, 93))
b = x(92)
