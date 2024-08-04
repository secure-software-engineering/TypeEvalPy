# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'nwvgb': 32, 'dpydx': 70, 'sjppn': 89}


def func2():
    return 30.59


def func3():
    return [85, 64, 23]


def func4():
    return 95


def func5():
    return (87, 3, 92)


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
