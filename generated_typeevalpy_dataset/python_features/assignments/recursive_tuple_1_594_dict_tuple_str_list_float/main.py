# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'gxbmg': 45, 'rhhbd': 21, 'hqxtl': 82}


def func2():
    return (61, 91, 30)


def func3():
    return 'lfzlh'


def func4():
    return [10, 68, 74]


def func5():
    return 39.35


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
