# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 96.88


def func2():
    return {'fvdjl': 42, 'svzfi': 32, 'nlndz': 100}


def func3():
    return [84, 36, 71]


def func4():
    return 'amobq'


def func5():
    return 44


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