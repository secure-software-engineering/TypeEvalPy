# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [6, 78, 54]


def func2():
    return 'shpjg'


def func3():
    return {'gpali': 70, 'baocd': 70, 'zjtvk': 17}


def func4():
    return 1.03


def func5():
    return 74


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
