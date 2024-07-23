# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 6.4


def func2():
    return (99, 38, 83)


def func3():
    return [95, 92, 44]


def func4():
    return {'qflth': 57, 'lcivk': 80, 'jtcmp': 71}


def func5():
    return 42


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
