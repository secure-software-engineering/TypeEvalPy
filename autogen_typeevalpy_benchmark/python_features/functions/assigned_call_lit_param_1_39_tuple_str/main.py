# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x((43, 13, 3))
b = x('uteua')
