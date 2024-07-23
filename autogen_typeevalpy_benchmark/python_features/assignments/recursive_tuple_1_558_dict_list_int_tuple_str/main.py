# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'bzusn': 18, 'oqaxb': 12, 'dabns': 37}


def func2():
    return [11, 95, 79]


def func3():
    return 9


def func4():
    return (20, 76, 100)


def func5():
    return 'kjrcx'


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
