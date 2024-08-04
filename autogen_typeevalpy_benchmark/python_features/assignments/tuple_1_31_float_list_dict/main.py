# Two variables are assigned a value via a tuple assignment.
def func1():
    return 38.9


def func2():
    return [40, 21, 53]


def func3():
    return {'imutl': 65, 'finlh': 67, 'yjdfs': 69}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
