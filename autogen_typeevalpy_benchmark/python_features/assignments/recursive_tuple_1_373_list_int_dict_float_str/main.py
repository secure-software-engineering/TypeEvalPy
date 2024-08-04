# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [4, 7, 9]


def func2():
    return 49


def func3():
    return {'nphhp': 7, 'wiluw': 94, 'nwyqq': 48}


def func4():
    return 22.83


def func5():
    return 'hamlh'


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
