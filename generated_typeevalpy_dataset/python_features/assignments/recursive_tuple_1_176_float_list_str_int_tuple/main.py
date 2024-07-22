# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 15.31


def func2():
    return [8, 30, 6]


def func3():
    return 'uomtt'


def func4():
    return 57


def func5():
    return (17, 72, 66)


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
