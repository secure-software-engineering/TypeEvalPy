# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 49


def func2():
    return [77, 41, 46]


def func3():
    return 'endof'


def func4():
    return 44.01


def func5():
    return (33, 96, 84)


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
