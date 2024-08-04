# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 56.26


def func2():
    return 21


def func3():
    return {'hhuab': 65, 'hpbhl': 86, 'ragjh': 99}


def func4():
    return 'oysdt'


def func5():
    return (56, 75, 11)


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
