# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'pwuih'


def func2():
    return 59


def func3():
    return (37, 56, 45)


def func4():
    return {'amftc': 69, 'qikxa': 91, 'djapu': 66}


def func5():
    return 75.01


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
