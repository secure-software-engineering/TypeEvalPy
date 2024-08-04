# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [42, 48, 74]


def func2():
    return (49, 51, 39)


def func3():
    return {'vewgl': 34, 'zdjsz': 84, 'gkyhz': 70}


def func4():
    return 58.77


def func5():
    return 'gxyvh'


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
