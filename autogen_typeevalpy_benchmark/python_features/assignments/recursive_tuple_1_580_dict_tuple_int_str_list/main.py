# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'iccde': 35, 'acgye': 9, 'fzyrf': 61}


def func2():
    return (47, 71, 96)


def func3():
    return 47


def func4():
    return 'ezqtr'


def func5():
    return [35, 75, 14]


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
