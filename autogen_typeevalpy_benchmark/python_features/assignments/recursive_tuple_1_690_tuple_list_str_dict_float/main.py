# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (51, 56, 93)


def func2():
    return [41, 86, 30]


def func3():
    return 'iossk'


def func4():
    return {'twoxt': 59, 'efxtk': 83, 'ydcme': 90}


def func5():
    return 93.47


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
