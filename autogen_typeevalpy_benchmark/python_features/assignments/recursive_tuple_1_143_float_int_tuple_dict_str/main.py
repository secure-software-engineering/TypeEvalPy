# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 53.02


def func2():
    return 17


def func3():
    return (90, 42, 76)


def func4():
    return {'yjqkb': 31, 'weccy': 14, 'mtzvt': 23}


def func5():
    return 'sjzxb'


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
