# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [35, 44, 8]


def func2():
    return 71


def func3():
    return 48.77


def func4():
    return (40, 78, 47)


def func5():
    return {'fkdii': 17, 'dibzr': 21, 'tsjlc': 79}


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
