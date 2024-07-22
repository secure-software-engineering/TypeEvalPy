# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 47


def func2():
    return (35, 62, 51)


def func3():
    return {'lgomm': 8, 'bcbhk': 68, 'hpmdz': 21}


def func4():
    return 44.28


def func5():
    return [20, 42, 18]


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
