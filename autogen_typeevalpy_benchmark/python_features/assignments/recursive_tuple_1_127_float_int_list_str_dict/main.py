# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 10.3


def func2():
    return 77


def func3():
    return [45, 73, 98]


def func4():
    return 'qlpom'


def func5():
    return {'wupav': 16, 'limii': 16, 'wesgb': 25}


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
