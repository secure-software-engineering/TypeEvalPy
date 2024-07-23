# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [86, 18, 48]


def func2():
    return 25.51


def func3():
    return {'sdhyp': 3, 'wocrc': 100, 'qcirt': 27}


def func4():
    return 'vnxnz'


def func5():
    return 34


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
