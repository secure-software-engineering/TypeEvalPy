# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'jbsub': 87, 'iouyr': 44, 'jlsbo': 43}


def func2():
    return 55


def func3():
    return 'horoj'


def func4():
    return 98.49


def func5():
    return (76, 42, 58)


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
