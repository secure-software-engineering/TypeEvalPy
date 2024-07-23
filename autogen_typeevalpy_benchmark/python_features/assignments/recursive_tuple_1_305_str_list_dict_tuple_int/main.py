# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'pwwyo'


def func2():
    return [74, 63, 33]


def func3():
    return {'uttmi': 86, 'rmljo': 68, 'vbgpo': 65}


def func4():
    return (80, 22, 47)


def func5():
    return 99


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
