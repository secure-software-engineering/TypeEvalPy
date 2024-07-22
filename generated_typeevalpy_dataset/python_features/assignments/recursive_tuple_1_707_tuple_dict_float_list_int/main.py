# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (55, 46, 65)


def func2():
    return {'aypgx': 99, 'aasje': 56, 'ltnbt': 100}


def func3():
    return 43.28


def func4():
    return [79, 88, 71]


def func5():
    return 91


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
