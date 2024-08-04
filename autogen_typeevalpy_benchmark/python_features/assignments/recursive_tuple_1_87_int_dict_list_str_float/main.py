# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 66


def func2():
    return {'jukhe': 91, 'efswu': 35, 'lsnhf': 71}


def func3():
    return [16, 22, 29]


def func4():
    return 'bgbdw'


def func5():
    return 92.8


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
