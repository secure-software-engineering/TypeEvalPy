# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 100


def func2():
    return 'plcld'


def func3():
    return 97.48


def func4():
    return {'xjxsu': 80, 'bubpl': 97, 'cbbwk': 53}


def func5():
    return [30, 77, 85]


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
