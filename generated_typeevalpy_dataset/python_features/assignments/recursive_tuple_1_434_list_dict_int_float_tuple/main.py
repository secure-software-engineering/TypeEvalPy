# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [92, 67, 14]


def func2():
    return {'cawgz': 45, 'wvvnb': 70, 'mtdjn': 43}


def func3():
    return 61


def func4():
    return 93.12


def func5():
    return (55, 33, 21)


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
