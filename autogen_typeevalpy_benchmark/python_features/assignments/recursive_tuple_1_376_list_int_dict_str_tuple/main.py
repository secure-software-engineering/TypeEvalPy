# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [86, 41, 17]


def func2():
    return 60


def func3():
    return {'moidf': 66, 'brhgb': 6, 'ywidk': 13}


def func4():
    return 'lhblr'


def func5():
    return (14, 51, 61)


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
