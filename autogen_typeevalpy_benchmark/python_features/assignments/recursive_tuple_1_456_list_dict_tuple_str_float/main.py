# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [46, 8, 2]


def func2():
    return {'ekvxc': 80, 'cfsew': 44, 'zrrgq': 5}


def func3():
    return (57, 37, 6)


def func4():
    return 'ymtsv'


def func5():
    return 46.91


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
