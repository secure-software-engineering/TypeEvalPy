# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ftgwn'


def func2():
    return {'lncdr': 87, 'ehpab': 90, 'jknmo': 72}


def func3():
    return [24, 59, 70]


def func4():
    return 17.52


def func5():
    return 83


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
