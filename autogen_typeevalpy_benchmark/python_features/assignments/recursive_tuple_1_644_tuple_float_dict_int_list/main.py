# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (29, 61, 50)


def func2():
    return 79.68


def func3():
    return {'tlhfc': 70, 'dghom': 96, 'nvuyc': 67}


def func4():
    return 100


def func5():
    return [92, 72, 46]


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
