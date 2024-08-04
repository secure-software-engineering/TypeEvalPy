# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [17, 97, 62]


def func2():
    return 1.67


def func3():
    return 'jgnot'


def func4():
    return 52


def func5():
    return {'edivv': 64, 'lbiun': 91, 'ullhe': 44}


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
