# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 76.83


def func2():
    return 'hwdqd'


def func3():
    return {'qbcbr': 46, 'wpbsb': 70, 'sggrw': 92}


def func4():
    return 6


def func5():
    return [77, 31, 45]


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
