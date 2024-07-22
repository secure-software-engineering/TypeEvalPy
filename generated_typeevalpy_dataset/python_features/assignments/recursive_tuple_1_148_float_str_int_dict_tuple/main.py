# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 89.92


def func2():
    return 'wlcrn'


def func3():
    return 26


def func4():
    return {'rdeoh': 75, 'bppux': 24, 'ogjwd': 3}


def func5():
    return (13, 87, 23)


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
