# Two variables are assigned a value via a tuple assignment.
def func1():
    return {'vmzau': 8, 'gogix': 44, 'dyiat': 5}


def func2():
    return 80


def func3():
    return (62, 54, 3)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
