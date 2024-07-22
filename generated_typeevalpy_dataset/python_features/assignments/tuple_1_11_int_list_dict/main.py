# Two variables are assigned a value via a tuple assignment.
def func1():
    return 94


def func2():
    return [45, 95, 85]


def func3():
    return {'bpfsi': 36, 'tnafp': 33, 'ftlis': 3}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
