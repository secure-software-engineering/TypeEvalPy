# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'agmtk': 88, 'pzblq': 64, 'mooph': 33}


def func2():
    return 56.36


def func3():
    return [88, 80, 74]


def func4():
    return 'hhyfp'


def func5():
    return (65, 39, 15)


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
