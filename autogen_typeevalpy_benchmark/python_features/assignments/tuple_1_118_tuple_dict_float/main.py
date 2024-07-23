# Two variables are assigned a value via a tuple assignment.
def func1():
    return (81, 98, 35)


def func2():
    return {'zgdvo': 79, 'chjsy': 26, 'swywt': 60}


def func3():
    return 74.44


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
