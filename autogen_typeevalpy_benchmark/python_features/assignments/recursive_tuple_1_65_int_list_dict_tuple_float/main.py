# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 38


def func2():
    return [29, 64, 88]


def func3():
    return {'lpdru': 91, 'spizd': 49, 'zsmvm': 8}


def func4():
    return (43, 20, 92)


def func5():
    return 21.85


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
