# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (40, 14, 15)


def func2():
    return [39, 29, 3]


def func3():
    return 82.94


def func4():
    return 32


def func5():
    return {'zxprc': 83, 'quhyb': 12, 'kxrrh': 20}


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
