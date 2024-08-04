# Two variables are assigned a value via a tuple assignment.
def func1():
    return 17


def func2():
    return {'slilo': 80, 'rqxjr': 85, 'mdzcd': 3}


def func3():
    return [38, 80, 46]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
