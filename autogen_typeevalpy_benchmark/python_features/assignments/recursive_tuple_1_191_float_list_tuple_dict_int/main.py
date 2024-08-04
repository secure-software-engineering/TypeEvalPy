# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 31.32


def func2():
    return [60, 70, 24]


def func3():
    return (97, 3, 57)


def func4():
    return {'vlolk': 65, 'vgjir': 14, 'hzwtx': 54}


def func5():
    return 55


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
