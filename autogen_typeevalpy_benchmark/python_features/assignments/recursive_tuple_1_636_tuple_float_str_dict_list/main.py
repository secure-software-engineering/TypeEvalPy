# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (73, 44, 67)


def func2():
    return 44.17


def func3():
    return 'bufzf'


def func4():
    return {'nshao': 28, 'jxgqb': 59, 'iegqb': 30}


def func5():
    return [97, 90, 76]


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
