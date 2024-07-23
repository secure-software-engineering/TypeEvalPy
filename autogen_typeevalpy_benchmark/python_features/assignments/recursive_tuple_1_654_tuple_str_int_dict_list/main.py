# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (63, 58, 91)


def func2():
    return 'tfnen'


def func3():
    return 12


def func4():
    return {'seyqt': 88, 'qdbew': 85, 'dizov': 7}


def func5():
    return [54, 65, 13]


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
