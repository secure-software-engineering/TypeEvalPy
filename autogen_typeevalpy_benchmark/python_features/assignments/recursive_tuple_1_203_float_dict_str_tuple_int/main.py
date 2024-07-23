# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 48.18


def func2():
    return {'nipwi': 83, 'utlrh': 59, 'zzpsp': 58}


def func3():
    return 'ayaom'


def func4():
    return (40, 15, 52)


def func5():
    return 93


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
