# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 94


def func2():
    return 'brywz'


def func3():
    return {'odyjh': 75, 'oippd': 82, 'ofqtx': 51}


def func4():
    return [33, 50, 2]


def func5():
    return (4, 78, 9)


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
