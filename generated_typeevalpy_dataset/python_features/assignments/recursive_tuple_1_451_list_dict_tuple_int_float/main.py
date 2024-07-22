# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [86, 71, 11]


def func2():
    return {'clhgt': 3, 'ijvxa': 15, 'fednf': 67}


def func3():
    return (4, 66, 7)


def func4():
    return 72


def func5():
    return 41.73


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
