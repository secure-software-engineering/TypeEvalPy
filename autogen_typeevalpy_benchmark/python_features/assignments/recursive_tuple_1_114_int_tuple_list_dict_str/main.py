# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 28


def func2():
    return (3, 34, 84)


def func3():
    return [64, 80, 31]


def func4():
    return {'lhvvz': 5, 'cnupo': 66, 'lrysq': 60}


def func5():
    return 'oiiqt'


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
