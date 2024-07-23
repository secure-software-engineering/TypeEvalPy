# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 93.77


def func2():
    return 99


def func3():
    return {'zehpm': 50, 'wtxtm': 98, 'zgsps': 78}


def func4():
    return (97, 18, 71)


def func5():
    return [56, 6, 16]


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
