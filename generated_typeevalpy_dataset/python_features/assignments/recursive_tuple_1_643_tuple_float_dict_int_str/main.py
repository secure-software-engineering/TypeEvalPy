# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (62, 34, 64)


def func2():
    return 76.47


def func3():
    return {'zqxfg': 97, 'azayo': 44, 'vpnrc': 58}


def func4():
    return 72


def func5():
    return 'wiqnj'


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
