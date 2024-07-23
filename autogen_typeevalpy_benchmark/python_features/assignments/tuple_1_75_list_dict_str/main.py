# Two variables are assigned a value via a tuple assignment.
def func1():
    return [98, 91, 56]


def func2():
    return {'qkfio': 23, 'wkssr': 63, 'zpaik': 29}


def func3():
    return 'fpgxw'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
