# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 37


def func2():
    return 69.38


def func3():
    return 'cmeem'


def func4():
    return {'uymgo': 30, 'zjgre': 16, 'wnuic': 72}


def func5():
    return [29, 63, 34]


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
