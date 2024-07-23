# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (64, 29, 49)


def func2():
    return 83


def func3():
    return {'ayfpg': 97, 'qljrz': 2, 'axjqz': 15}


def func4():
    return [11, 62, 56]


def func5():
    return 'fvugw'


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
