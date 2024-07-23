# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 94.02


def func2():
    return (46, 79, 53)


def func3():
    return 96


def func4():
    return 'izzsa'


def func5():
    return {'wqfib': 37, 'wmbou': 53, 'awtaj': 4}


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
