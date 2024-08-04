# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [72, 89, 97]


def func2():
    return {'giguz': 10, 'gaygq': 15, 'hmtwv': 18}


def func3():
    return 25


def func4():
    return 'eslup'


def func5():
    return 73.91


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
