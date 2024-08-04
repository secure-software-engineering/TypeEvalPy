# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 8


def func2():
    return 43.06


def func3():
    return [17, 61, 28]


def func4():
    return (58, 10, 48)


def func5():
    return {'rkouw': 59, 'pqzry': 17, 'tkenm': 91}


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
