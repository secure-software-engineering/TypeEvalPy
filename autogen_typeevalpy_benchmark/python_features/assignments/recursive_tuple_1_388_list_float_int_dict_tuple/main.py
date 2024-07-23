# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [60, 59, 9]


def func2():
    return 54.34


def func3():
    return 20


def func4():
    return {'xuhcr': 47, 'mlzxf': 48, 'hovyz': 67}


def func5():
    return (87, 28, 21)


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
