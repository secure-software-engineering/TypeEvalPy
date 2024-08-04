# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'cosgu': 82, 'iyupt': 49, 'zhoml': 74}


def func2():
    return (26, 27, 31)


def func3():
    return 'tpzlc'


def func4():
    return 80


def func5():
    return [8, 22, 44]


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
