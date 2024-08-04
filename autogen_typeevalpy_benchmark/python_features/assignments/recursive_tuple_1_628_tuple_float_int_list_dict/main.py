# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (61, 1, 7)


def func2():
    return 29.22


def func3():
    return 76


def func4():
    return [32, 2, 92]


def func5():
    return {'ixdha': 99, 'tpuoe': 95, 'uafjt': 94}


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
