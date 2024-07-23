# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'zsksd': 8, 'cmfhc': 74, 'tnmvz': 88}


def func2():
    return 'bhpeh'


def func3():
    return [5, 36, 70]


def func4():
    return (3, 83, 49)


def func5():
    return 48.86


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
