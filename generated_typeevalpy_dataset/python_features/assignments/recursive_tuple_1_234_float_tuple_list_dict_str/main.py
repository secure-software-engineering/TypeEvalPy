# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 55.66


def func2():
    return (35, 87, 73)


def func3():
    return [48, 28, 50]


def func4():
    return {'oowkh': 41, 'gzaob': 69, 'ydwog': 49}


def func5():
    return 'eqltg'


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
