# Two variables are assigned a value via a tuple assignment.
def func1():
    return [13, 28, 73]


def func2():
    return {'cemjq': 89, 'nhrsz': 65, 'xgkna': 100}


def func3():
    return 97.94


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
