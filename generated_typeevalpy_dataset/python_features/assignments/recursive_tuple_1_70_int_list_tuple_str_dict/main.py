# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 88


def func2():
    return [33, 62, 45]


def func3():
    return (93, 26, 35)


def func4():
    return 'kkfhy'


def func5():
    return {'kftop': 60, 'qrgft': 75, 'eygll': 53}


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
