# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'rcdyv': 63, 'efarb': 66, 'egfzh': 73}


def func2():
    return 77.48


def func3():
    return 'scmpd'


def func4():
    return [98, 53, 76]


def func5():
    return 79


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
