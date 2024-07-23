# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 36.22


def func2():
    return 85


def func3():
    return {'vnxdo': 51, 'upzhm': 28, 'pidsi': 73}


def func4():
    return [62, 30, 27]


def func5():
    return 'bjyof'


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
