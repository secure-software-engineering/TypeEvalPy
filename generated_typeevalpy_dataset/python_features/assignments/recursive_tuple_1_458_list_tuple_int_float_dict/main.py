# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [34, 35, 21]


def func2():
    return (85, 26, 29)


def func3():
    return 13


def func4():
    return 26.11


def func5():
    return {'ljcny': 3, 'oxmgm': 62, 'zzytl': 54}


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
