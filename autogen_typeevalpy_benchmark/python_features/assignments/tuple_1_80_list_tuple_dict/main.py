# Two variables are assigned a value via a tuple assignment.
def func1():
    return [1, 92, 44]


def func2():
    return (20, 55, 80)


def func3():
    return {'qbtev': 32, 'qxppq': 46, 'jfyve': 52}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
