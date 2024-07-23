# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 4


def func2():
    return {'vmwyp': 73, 'imnys': 75, 'oezjx': 70}


def func3():
    return [2, 87, 98]


def func4():
    return 'mwrvw'


def func5():
    return 69.34


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
