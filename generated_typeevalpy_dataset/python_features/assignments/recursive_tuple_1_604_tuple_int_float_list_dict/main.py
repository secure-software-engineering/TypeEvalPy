# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (49, 88, 35)


def func2():
    return 58


def func3():
    return 49.03


def func4():
    return [48, 77, 64]


def func5():
    return {'aipzo': 4, 'jphxm': 61, 'jaepi': 55}


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
