# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 81.0


def func2():
    return 'nunpi'


def func3():
    return {'fvasj': 68, 'zccyf': 7, 'nookt': 78}


def func4():
    return [61, 85, 68]


def func5():
    return 67


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
