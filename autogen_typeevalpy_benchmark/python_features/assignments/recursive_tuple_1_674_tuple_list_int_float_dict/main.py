# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (86, 70, 46)


def func2():
    return [84, 13, 91]


def func3():
    return 40


def func4():
    return 88.26


def func5():
    return {'byyrm': 52, 'qcdvy': 70, 'cozum': 86}


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
