# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 90


def func2():
    return [81, 100, 22]


def func3():
    return {'ucnxz': 30, 'wjawc': 21, 'juchp': 51}


def func4():
    return 87.58


def func5():
    return 'wiguu'


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
