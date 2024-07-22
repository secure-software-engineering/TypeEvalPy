# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'oofog'


def func2():
    return {'gdaow': 10, 'qoqrs': 62, 'exyfx': 12}


def func3():
    return 66.56


def func4():
    return (98, 15, 85)


def func5():
    return [6, 1, 30]


def func6():
    pass


a, (b, c) = func1, (func2, func3)
i = a()
j = b()
k = c()

a, (b, (c, d)) = func1, (func2, (func3, func4))

h = d()

f, b = c, e = func5, func6

l = e()
m = f()
