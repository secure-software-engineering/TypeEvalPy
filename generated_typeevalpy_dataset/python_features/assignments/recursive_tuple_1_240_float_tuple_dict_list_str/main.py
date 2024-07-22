# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 9.89


def func2():
    return (36, 100, 98)


def func3():
    return {'hduub': 45, 'woktn': 40, 'tkzrk': 25}


def func4():
    return [59, 24, 64]


def func5():
    return 'qdsay'


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
