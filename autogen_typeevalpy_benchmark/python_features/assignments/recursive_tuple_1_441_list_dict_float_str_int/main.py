# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [67, 66, 7]


def func2():
    return {'sofdb': 81, 'deeab': 77, 'nljba': 86}


def func3():
    return 86.92


def func4():
    return 'xrsdo'


def func5():
    return 38


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
