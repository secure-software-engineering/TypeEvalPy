# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 89.95


def func2():
    return 'sbmpp'


def func3():
    return 14


def func4():
    return (58, 9, 23)


def func5():
    return [63, 7, 62]


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
