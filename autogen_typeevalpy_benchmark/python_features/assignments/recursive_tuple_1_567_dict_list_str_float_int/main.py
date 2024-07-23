# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'rvgmw': 28, 'gyxaa': 77, 'kuefh': 64}


def func2():
    return [7, 67, 25]


def func3():
    return 'rpkfj'


def func4():
    return 99.61


def func5():
    return 46


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
