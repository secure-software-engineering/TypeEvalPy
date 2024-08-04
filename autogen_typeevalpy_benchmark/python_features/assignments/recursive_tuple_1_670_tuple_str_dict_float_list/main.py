# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (15, 42, 81)


def func2():
    return 'tvupt'


def func3():
    return {'plwqn': 38, 'wdqhu': 4, 'glhkm': 98}


def func4():
    return 98.98


def func5():
    return [99, 55, 93]


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
