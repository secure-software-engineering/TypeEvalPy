# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 55.4


def func2():
    return 'ddqxj'


def func3():
    return 44


def func4():
    return (56, 8, 31)


def func5():
    return {'gpftx': 45, 'uozas': 78, 'vbdeb': 84}


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
