# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (18, 98, 75)


def func2():
    return 34.42


def func3():
    return [53, 66, 23]


def func4():
    return 82


def func5():
    return {'ywdeb': 47, 'etobu': 13, 'dukzt': 10}


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
