# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'bhvkk': 11, 'flonl': 84, 'ryosc': 58}


def func2():
    return 54


def func3():
    return (70, 94, 8)


def func4():
    return 'ttdep'


def func5():
    return 15.38


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
