# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'flnri'


def func2():
    return 73


def func3():
    return 80.04


def func4():
    return (66, 53, 19)


def func5():
    return {'tzpwz': 100, 'btpub': 98, 'bkefz': 23}


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
