# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 87


def func2():
    return 90.6


def func3():
    return 'wgbao'


def func4():
    return [71, 9, 35]


def func5():
    return {'xkmmy': 78, 'jsahe': 92, 'igfxi': 85}


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
