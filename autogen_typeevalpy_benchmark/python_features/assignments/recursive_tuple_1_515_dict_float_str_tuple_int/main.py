# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'hxxoa': 90, 'jryvq': 56, 'ropbk': 21}


def func2():
    return 82.44


def func3():
    return 'tyweo'


def func4():
    return (27, 65, 79)


def func5():
    return 50


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
