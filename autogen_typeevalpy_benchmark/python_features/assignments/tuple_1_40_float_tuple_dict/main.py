# Two variables are assigned a value via a tuple assignment.
def func1():
    return 53.54


def func2():
    return (65, 12, 61)


def func3():
    return {'nbsyw': 6, 'dodpf': 27, 'lxnmh': 28}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
