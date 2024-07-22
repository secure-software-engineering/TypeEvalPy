# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 41


def func2():
    return {'uniaq': 62, 'sihgl': 52, 'puecv': 29}


def func3():
    return 'kljvi'


def func4():
    return 82.76


def func5():
    return (10, 71, 47)


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
