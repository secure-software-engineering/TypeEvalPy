# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'xjsbp'


def func2():
    return 20.19


def func3():
    return 80


def func4():
    return {'dnxsl': 22, 'vckat': 87, 'onacu': 12}


def func5():
    return (54, 74, 61)


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
