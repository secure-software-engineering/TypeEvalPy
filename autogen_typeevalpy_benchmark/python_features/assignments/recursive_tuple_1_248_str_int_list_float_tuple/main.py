# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'cgwbo'


def func2():
    return 88


def func3():
    return [48, 13, 22]


def func4():
    return 1.17


def func5():
    return (68, 2, 1)


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
