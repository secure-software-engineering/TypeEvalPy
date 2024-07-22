# Two variables are assigned a value via a tuple assignment.
def func1():
    return (77, 99, 17)


def func2():
    return 29


def func3():
    return {'deudi': 97, 'eqlpw': 74, 'mmzqs': 39}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
