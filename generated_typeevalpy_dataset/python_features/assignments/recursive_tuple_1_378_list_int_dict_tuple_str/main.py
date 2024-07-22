# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [85, 8, 72]


def func2():
    return 42


def func3():
    return {'ilufa': 93, 'qmtzy': 36, 'fenle': 93}


def func4():
    return (24, 76, 13)


def func5():
    return 'sjpkr'


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
