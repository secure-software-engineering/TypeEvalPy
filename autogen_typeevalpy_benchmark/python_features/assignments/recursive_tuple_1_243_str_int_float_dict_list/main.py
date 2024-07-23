# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'otvxl'


def func2():
    return 94


def func3():
    return 80.49


def func4():
    return {'mojgo': 9, 'mzbhe': 64, 'dfzxe': 13}


def func5():
    return [14, 33, 82]


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
