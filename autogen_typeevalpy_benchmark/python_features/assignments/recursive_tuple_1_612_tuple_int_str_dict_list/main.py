# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (81, 36, 12)


def func2():
    return 10


def func3():
    return 'kayrs'


def func4():
    return {'wkcuk': 25, 'donvg': 87, 'dbtex': 34}


def func5():
    return [36, 35, 28]


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
