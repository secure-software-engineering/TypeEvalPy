# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x((57, 84, 81))
b = x([86, 49, 38])
