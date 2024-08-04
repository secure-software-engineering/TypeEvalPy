# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'iycsv': 72, 'tnxdm': 16, 'lxazu': 14}


def func2():
    return 'tvvut'


def func3():
    return [5, 26, 40]


def func4():
    return 27


def func5():
    return (76, 65, 98)


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
