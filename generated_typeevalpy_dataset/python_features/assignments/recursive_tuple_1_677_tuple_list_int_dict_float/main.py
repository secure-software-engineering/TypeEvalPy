# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (37, 28, 62)


def func2():
    return [49, 34, 77]


def func3():
    return 26


def func4():
    return {'kgiig': 4, 'jsknq': 29, 'aqwbc': 95}


def func5():
    return 66.58


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
