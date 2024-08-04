# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'lnttc': 43, 'uljhu': 30, 'ofhxf': 63}


def func2():
    return 'nafnk'


def func3():
    return 9


def func4():
    return 69.15


def func5():
    return [31, 83, 67]


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
