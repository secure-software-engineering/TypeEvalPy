# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 23


def func2():
    return 7.47


def func3():
    return (17, 96, 9)


def func4():
    return {'dywws': 87, 'hwazr': 84, 'prwal': 7}


def func5():
    return [42, 56, 53]


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
