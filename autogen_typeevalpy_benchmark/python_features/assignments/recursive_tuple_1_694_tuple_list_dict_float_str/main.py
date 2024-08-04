# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (18, 96, 75)


def func2():
    return [76, 81, 39]


def func3():
    return {'akonr': 53, 'zcqsj': 88, 'hlqlr': 71}


def func4():
    return 23.2


def func5():
    return 'ipayc'


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
