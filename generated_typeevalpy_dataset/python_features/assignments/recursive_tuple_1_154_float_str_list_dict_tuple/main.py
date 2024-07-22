# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 33.9


def func2():
    return 'ezttp'


def func3():
    return [58, 16, 81]


def func4():
    return {'ktten': 60, 'vakis': 21, 'stenk': 36}


def func5():
    return (4, 52, 74)


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
