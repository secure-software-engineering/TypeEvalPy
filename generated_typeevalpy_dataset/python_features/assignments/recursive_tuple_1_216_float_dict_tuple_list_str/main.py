# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 34.25


def func2():
    return {'zkmtm': 75, 'jhqky': 6, 'khpij': 74}


def func3():
    return (93, 52, 45)


def func4():
    return [61, 26, 92]


def func5():
    return 'cpllh'


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
