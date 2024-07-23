# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 97.11


def func2():
    return 59


def func3():
    return 'zkmqy'


def func4():
    return {'ghote': 10, 'hkmld': 44, 'ogxhp': 68}


def func5():
    return (66, 78, 99)


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
