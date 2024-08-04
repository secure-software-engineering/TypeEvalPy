# Call a function assigned to a variable with a literal parameter.


def func(x):
    return x


x = func
a = x(51)
b = x({'wmusd': 73, 'fhbgb': 61, 'gbcal': 13})
