# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'qffpg': 69, 'edhbs': 23, 'uwdqe': 44}


def func2():
    return 33


def func3():
    return 86.85


def func4():
    return 'zaqfk'


def func5():
    return [22, 82, 62]


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
