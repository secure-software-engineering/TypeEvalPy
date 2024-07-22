# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'svody': 18, 'zbzvi': 94, 'ztuvz': 24}


def func2():
    return 'fgpws'


def func3():
    return [8, 3, 61]


def func4():
    return 82


def func5():
    return (28, 47, 70)


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
