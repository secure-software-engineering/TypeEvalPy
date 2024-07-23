# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [86, 17, 95]


def func2():
    return (21, 35, 22)


def func3():
    return 'luzhs'


def func4():
    return 62


def func5():
    return {'jrcrd': 34, 'jrvyy': 60, 'wekos': 99}


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
