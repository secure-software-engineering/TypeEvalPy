# Two variables are assigned a value via a tuple assignment.
def func1():
    return (75, 38, 25)


def func2():
    return {'dcnah': 9, 'kgtuq': 100, 'rtoda': 84}


def func3():
    return 9


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
