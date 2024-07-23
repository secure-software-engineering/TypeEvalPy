# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ilasp': 44, 'konag': 15, 'cdvwr': 41}


def func2():
    return [83, 40, 71]


def func3():
    return (9, 5, 3)


def func4():
    return 'sqopo'


def func5():
    return 76


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
