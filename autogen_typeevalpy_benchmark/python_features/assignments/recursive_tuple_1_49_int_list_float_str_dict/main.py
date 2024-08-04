# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 30


def func2():
    return [65, 76, 91]


def func3():
    return 98.85


def func4():
    return 'gqxit'


def func5():
    return {'tqbjh': 98, 'dfayp': 6, 'ytihq': 67}


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
