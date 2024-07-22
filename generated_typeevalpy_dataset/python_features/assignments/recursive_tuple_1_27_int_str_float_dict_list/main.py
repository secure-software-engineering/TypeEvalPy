# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 70


def func2():
    return 'yqqzf'


def func3():
    return 28.1


def func4():
    return {'dgdmr': 40, 'ogwba': 23, 'qkkjo': 34}


def func5():
    return [26, 83, 39]


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
