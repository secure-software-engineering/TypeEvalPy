# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [59, 46, 40]


def func2():
    return 76.69


def func3():
    return {'fwsxt': 49, 'rybzs': 80, 'mqlyy': 71}


def func4():
    return 'fusvt'


def func5():
    return (6, 8, 71)


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
