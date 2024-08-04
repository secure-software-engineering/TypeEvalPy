# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ihuoj'


def func2():
    return 9


def func3():
    return [23, 25, 82]


def func4():
    return {'qefiw': 5, 'xpoxs': 69, 'wedva': 16}


def func5():
    return 80.91


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
