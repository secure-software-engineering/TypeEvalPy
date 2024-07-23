# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'clwna'


def func2():
    return (3, 97, 1)


def func3():
    return 57


def func4():
    return 49.47


def func5():
    return {'hbido': 69, 'xuuvj': 8, 'xfrto': 96}


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
