# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (54, 98, 88)


def func2():
    return 5.95


def func3():
    return {'ljpxb': 18, 'aiplh': 38, 'nxnks': 24}


def func4():
    return [89, 15, 35]


def func5():
    return 86


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
