# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 42.76


def func2():
    return (33, 12, 4)


def func3():
    return {'fnvfz': 61, 'uupgb': 8, 'hbzik': 70}


def func4():
    return 'mszox'


def func5():
    return 44


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
