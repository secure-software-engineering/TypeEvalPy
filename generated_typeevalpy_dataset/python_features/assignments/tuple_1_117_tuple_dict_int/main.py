# Two variables are assigned a value via a tuple assignment.
def func1():
    return (11, 33, 18)


def func2():
    return {'wviuw': 44, 'bwbjr': 21, 'vxhhi': 45}


def func3():
    return 4


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
