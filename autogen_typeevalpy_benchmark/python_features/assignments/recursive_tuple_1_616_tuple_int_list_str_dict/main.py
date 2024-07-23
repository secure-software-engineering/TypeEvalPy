# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (75, 57, 36)


def func2():
    return 15


def func3():
    return [68, 56, 69]


def func4():
    return 'fofhc'


def func5():
    return {'pgsjj': 87, 'ghaif': 23, 'htqix': 65}


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
