# Two variables are assigned a value via a tuple assignment.
def func1():
    return [30, 38, 21]


def func2():
    return {'jmdye': 28, 'emyzy': 63, 'qxgur': 53}


def func3():
    return (46, 27, 62)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
