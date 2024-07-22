# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [20, 13, 100]


def func2():
    return {'rrqeq': 14, 'uhgwj': 100, 'vnerq': 13}


def func3():
    return 57.56


def func4():
    return 'susrk'


def func5():
    return 5


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
