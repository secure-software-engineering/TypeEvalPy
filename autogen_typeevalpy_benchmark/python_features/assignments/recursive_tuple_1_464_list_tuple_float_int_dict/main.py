# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [13, 47, 65]


def func2():
    return (76, 96, 87)


def func3():
    return 98.35


def func4():
    return 54


def func5():
    return {'zyhil': 26, 'wimvx': 46, 'kcwhb': 26}


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
