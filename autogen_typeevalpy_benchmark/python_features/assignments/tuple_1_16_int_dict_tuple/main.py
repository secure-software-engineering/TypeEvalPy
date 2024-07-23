# Two variables are assigned a value via a tuple assignment.
def func1():
    return 44


def func2():
    return {'qlnhi': 22, 'fbycy': 66, 'mrklq': 53}


def func3():
    return (28, 26, 40)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
