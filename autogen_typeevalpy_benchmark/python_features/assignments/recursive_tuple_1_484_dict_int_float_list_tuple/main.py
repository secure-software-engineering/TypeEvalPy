# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ykyog': 9, 'nqyna': 48, 'pneyr': 86}


def func2():
    return 27


def func3():
    return 38.99


def func4():
    return [39, 22, 13]


def func5():
    return (38, 70, 39)


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
