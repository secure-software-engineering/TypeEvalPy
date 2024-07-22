# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 95.92


def func2():
    return {'trvst': 76, 'ajifv': 14, 'lzvhy': 87}


def func3():
    return 'tqdjk'


def func4():
    return (74, 36, 43)


def func5():
    return 6


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
