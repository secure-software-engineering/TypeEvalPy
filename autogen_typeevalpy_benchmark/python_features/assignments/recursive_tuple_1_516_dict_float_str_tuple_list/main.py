# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'rwfvk': 32, 'tnqwz': 56, 'xttel': 71}


def func2():
    return 31.17


def func3():
    return 'uaben'


def func4():
    return (21, 26, 29)


def func5():
    return [92, 78, 20]


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
