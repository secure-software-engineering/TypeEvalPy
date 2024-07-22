# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x({'phuky': 67, 'vsuri': 17, 'frnfp': 87})
b = x((30, 13, 66))
