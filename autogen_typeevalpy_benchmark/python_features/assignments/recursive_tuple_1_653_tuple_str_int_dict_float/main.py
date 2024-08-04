# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (57, 80, 35)


def func2():
    return 'oufrg'


def func3():
    return 1


def func4():
    return {'wwlfu': 58, 'boodc': 88, 'kakji': 65}


def func5():
    return 41.23


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
