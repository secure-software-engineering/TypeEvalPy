# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 68


def func2():
    return {'shvmn': 69, 'swopx': 71, 'eykit': 77}


def func3():
    return 88.32


def func4():
    return [52, 62, 76]


def func5():
    return 'daned'


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
