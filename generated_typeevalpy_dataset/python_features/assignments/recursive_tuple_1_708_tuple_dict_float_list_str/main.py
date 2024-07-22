# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (58, 92, 93)


def func2():
    return {'afvmb': 32, 'yhmqe': 82, 'oofri': 7}


def func3():
    return 49.47


def func4():
    return [15, 22, 37]


def func5():
    return 'doppj'


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
