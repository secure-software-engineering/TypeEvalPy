# Two variables are assigned a value via a tuple assignment.
def func1():
    return [41, 84, 42]


def func2():
    return (16, 37, 60)


def func3():
    return {'jtdib': 60, 'nuywp': 50, 'xeohw': 84}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
