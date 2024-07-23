# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 91.04


def func2():
    return 40


def func3():
    return (53, 70, 79)


def func4():
    return {'kcint': 24, 'kfmms': 87, 'qhsdk': 26}


def func5():
    return 'jtang'


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
