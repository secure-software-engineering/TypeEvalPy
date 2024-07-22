# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 57.27


def func2():
    return [10, 44, 15]


def func3():
    return 'msqkm'


def func4():
    return {'fjjmj': 31, 'tnmxq': 36, 'cikkp': 28}


def func5():
    return (9, 30, 70)


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
