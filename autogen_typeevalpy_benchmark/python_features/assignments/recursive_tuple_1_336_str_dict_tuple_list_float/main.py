# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'gkrwo'


def func2():
    return {'svmgl': 16, 'pkvhd': 91, 'zkphq': 54}


def func3():
    return (33, 83, 78)


def func4():
    return [64, 1, 15]


def func5():
    return 41.15


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
