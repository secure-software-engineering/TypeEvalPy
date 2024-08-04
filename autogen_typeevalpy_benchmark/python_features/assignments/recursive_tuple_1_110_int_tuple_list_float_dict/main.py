# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 28


def func2():
    return (45, 27, 25)


def func3():
    return [87, 74, 2]


def func4():
    return 37.66


def func5():
    return {'jhhvd': 48, 'mzkjv': 23, 'lziyl': 71}


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
