# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [62, 24, 3]


def func2():
    return 'xtuga'


def func3():
    return {'bcvsw': 13, 'xovkd': 30, 'xeimu': 31}


def func4():
    return (62, 70, 23)


def func5():
    return 72.53


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
