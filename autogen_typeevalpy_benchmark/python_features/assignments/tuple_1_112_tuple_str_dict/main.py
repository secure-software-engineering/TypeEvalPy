# Two variables are assigned a value via a tuple assignment.
def func1():
    return (74, 6, 54)


def func2():
    return 'tesuk'


def func3():
    return {'xjoak': 78, 'xtfqz': 30, 'mcplm': 35}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
