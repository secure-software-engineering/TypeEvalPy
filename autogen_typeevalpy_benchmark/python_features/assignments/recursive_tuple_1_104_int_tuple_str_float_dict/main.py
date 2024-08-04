# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 61


def func2():
    return (33, 98, 57)


def func3():
    return 'qddob'


def func4():
    return 86.04


def func5():
    return {'kwxdj': 95, 'vyjrn': 32, 'gwrqq': 90}


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
