# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ortuj': 43, 'pqjjv': 48, 'rggcc': 14}


def func2():
    return 76.68


def func3():
    return [26, 76, 1]


def func4():
    return (78, 22, 57)


def func5():
    return 'bsldr'


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
