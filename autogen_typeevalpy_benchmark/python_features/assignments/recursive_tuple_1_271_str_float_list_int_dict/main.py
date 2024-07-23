# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'crlgk'


def func2():
    return 96.82


def func3():
    return [81, 56, 18]


def func4():
    return 18


def func5():
    return {'morbx': 74, 'gwxmz': 35, 'eljpi': 71}


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
