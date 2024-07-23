# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'gzgci': 26, 'iqwts': 40, 'wftdf': 53}


def func2():
    return [69, 1, 95]


def func3():
    return 30.69


def func4():
    return 34


def func5():
    return (87, 50, 82)


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
