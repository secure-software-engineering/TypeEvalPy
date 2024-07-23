# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'namrb'


def func2():
    return [25, 7, 41]


def func3():
    return 13


def func4():
    return (98, 16, 75)


def func5():
    return {'nmrlc': 16, 'tyviu': 40, 'kftxk': 90}


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
