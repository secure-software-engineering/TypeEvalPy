# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 40.67


def func2():
    return {'etstc': 74, 'xzuoz': 61, 'qousb': 28}


def func3():
    return 'tltuh'


def func4():
    return 86


def func5():
    return [6, 78, 52]


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
