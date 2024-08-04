# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'fblaj'


def func2():
    return {'zyqkv': 93, 'zwcvp': 98, 'oddmz': 44}


def func3():
    return (16, 80, 5)


def func4():
    return 82


def func5():
    return [41, 32, 40]


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
