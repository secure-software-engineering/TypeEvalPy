# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'tkjna'


def func2():
    return [68, 86, 35]


def func3():
    return 58.97


def func4():
    return (2, 39, 18)


def func5():
    return {'igmfr': 98, 'mfeoq': 9, 'wbrwd': 62}


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
