# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [26, 74, 27]


def func2():
    return {'givmt': 19, 'bjtkv': 43, 'onbiy': 81}


def func3():
    return (13, 30, 51)


def func4():
    return 'mqdgr'


def func5():
    return 60


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
