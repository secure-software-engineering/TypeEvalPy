# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 85


def func2():
    return (87, 47, 31)


def func3():
    return 43.23


def func4():
    return {'uxnar': 13, 'olsgs': 10, 'fcqak': 36}


def func5():
    return 'vnzxy'


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
