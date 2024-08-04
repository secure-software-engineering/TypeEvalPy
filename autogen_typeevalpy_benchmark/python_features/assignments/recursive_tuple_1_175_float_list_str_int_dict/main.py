# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 25.22


def func2():
    return [3, 64, 94]


def func3():
    return 'kjocf'


def func4():
    return 4


def func5():
    return {'kgjoq': 61, 'ivzce': 67, 'wmgdq': 93}


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
