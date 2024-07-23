# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 41


def func2():
    return {'erkqg': 98, 'qzwrw': 44, 'wbirs': 73}


def func3():
    return (91, 89, 49)


def func4():
    return 'qwbkb'


def func5():
    return [63, 76, 45]


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
