# Two variables are assigned a value via a tuple assignment.
def func1():
    return (45, 59, 84)


def func2():
    return 78.07


def func3():
    return {'xptjp': 65, 'idaeq': 25, 'lyufx': 6}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
