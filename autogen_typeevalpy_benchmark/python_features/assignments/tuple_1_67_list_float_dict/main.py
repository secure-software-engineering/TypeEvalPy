# Two variables are assigned a value via a tuple assignment.
def func1():
    return [61, 77, 83]


def func2():
    return 96.23


def func3():
    return {'gepmu': 77, 'jeahc': 62, 'pjydf': 46}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
