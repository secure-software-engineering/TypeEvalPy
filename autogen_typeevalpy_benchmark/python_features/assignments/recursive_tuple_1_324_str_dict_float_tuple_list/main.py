# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ixlff'


def func2():
    return {'mzldb': 63, 'vsjcv': 77, 'plngn': 80}


def func3():
    return 69.26


def func4():
    return (17, 14, 52)


def func5():
    return [38, 79, 70]


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
