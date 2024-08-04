# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (31, 88, 24)


def func2():
    return 3.15


def func3():
    return {'crale': 87, 'tehdy': 62, 'mbpdp': 43}


def func4():
    return 42


def func5():
    return [11, 43, 35]


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
