# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [78, 78, 45]


def func2():
    return 'fbsre'


def func3():
    return (24, 16, 23)


def func4():
    return {'detlz': 12, 'mridi': 48, 'bachz': 65}


def func5():
    return 81.71


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
