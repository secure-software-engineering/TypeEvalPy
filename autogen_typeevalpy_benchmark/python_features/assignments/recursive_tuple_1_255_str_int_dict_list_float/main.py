# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'wtldc'


def func2():
    return 20


def func3():
    return {'hblqa': 1, 'hwjiq': 95, 'gzdpc': 77}


def func4():
    return [44, 17, 30]


def func5():
    return 75.63


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
