# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 27


def func2():
    return 'nmbst'


def func3():
    return (49, 44, 96)


def func4():
    return 40.53


def func5():
    return {'fagsd': 3, 'rmlcr': 78, 'slmhe': 13}


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
