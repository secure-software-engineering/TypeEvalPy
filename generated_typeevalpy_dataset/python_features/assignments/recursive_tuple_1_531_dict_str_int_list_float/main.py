# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'layxa': 37, 'nomic': 96, 'zanzo': 89}


def func2():
    return 'gkzyp'


def func3():
    return 22


def func4():
    return [42, 48, 55]


def func5():
    return 41.29


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
