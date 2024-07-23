# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'qammq': 64, 'yyzko': 54, 'zqyxv': 6}


def func2():
    return [85, 36, 32]


def func3():
    return (10, 7, 25)


def func4():
    return 'xmzbu'


def func5():
    return 87.58


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
