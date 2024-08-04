# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 60.88


def func2():
    return [20, 13, 95]


def func3():
    return 76


def func4():
    return (51, 25, 78)


def func5():
    return {'wulth': 90, 'lczoj': 69, 'lfkhh': 65}


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
