# Two variables are assigned a value via a tuple assignment.
def func1():
    return {'mbmsw': 56, 'xphvo': 55, 'tmgsx': 17}


def func2():
    return 20.55


def func3():
    return (73, 44, 54)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
