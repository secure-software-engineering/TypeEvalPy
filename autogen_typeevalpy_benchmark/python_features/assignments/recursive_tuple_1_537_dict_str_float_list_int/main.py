# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'xpvuv': 73, 'czhqe': 41, 'iohot': 21}


def func2():
    return 'txcqf'


def func3():
    return 92.84


def func4():
    return [8, 84, 97]


def func5():
    return 4


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
