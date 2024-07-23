# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'jkgsx': 20, 'lwequ': 55, 'wpudl': 14}


def func2():
    return 8.96


def func3():
    return 'qljus'


def func4():
    return [1, 69, 88]


def func5():
    return (5, 66, 32)


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
