# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [94, 21, 85]


def func2():
    return 88


def func3():
    return (10, 72, 84)


def func4():
    return 20.91


def func5():
    return 'tudow'


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
