# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [29, 3, 1]


def func2():
    return (51, 63, 59)


def func3():
    return 49


def func4():
    return {'twiae': 75, 'jamzi': 8, 'dkhlg': 81}


def func5():
    return 19.49


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
