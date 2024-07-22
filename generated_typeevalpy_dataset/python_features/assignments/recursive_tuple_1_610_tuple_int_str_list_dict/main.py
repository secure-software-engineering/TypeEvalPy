# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (41, 63, 26)


def func2():
    return 18


def func3():
    return 'rbzeo'


def func4():
    return [3, 15, 44]


def func5():
    return {'qauxg': 84, 'adfbr': 9, 'tpzzg': 81}


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
