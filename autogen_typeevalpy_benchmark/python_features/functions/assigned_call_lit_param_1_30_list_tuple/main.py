# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x([24, 62, 74])
b = x((57, 13, 82))
