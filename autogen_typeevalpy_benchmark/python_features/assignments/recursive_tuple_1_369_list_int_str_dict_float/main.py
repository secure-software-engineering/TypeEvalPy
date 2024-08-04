# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [56, 52, 73]


def func2():
    return 72


def func3():
    return 'ybqao'


def func4():
    return {'eqlkx': 84, 'qefoz': 32, 'fpirx': 67}


def func5():
    return 14.71


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
