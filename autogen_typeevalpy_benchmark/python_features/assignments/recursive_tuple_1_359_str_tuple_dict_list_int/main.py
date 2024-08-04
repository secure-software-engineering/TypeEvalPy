# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'slmwd'


def func2():
    return (7, 78, 26)


def func3():
    return {'gcrmd': 42, 'qzbka': 50, 'bcttm': 13}


def func4():
    return [60, 65, 53]


def func5():
    return 100


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
