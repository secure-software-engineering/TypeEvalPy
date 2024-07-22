# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'wtzqk': 25, 'aaqhb': 1, 'mcjdz': 11}


def func2():
    return (7, 99, 42)


def func3():
    return 71.75


def func4():
    return [92, 82, 100]


def func5():
    return 'uvoav'


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
