# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [8, 30, 77]


def func2():
    return 'nuufi'


def func3():
    return (53, 91, 83)


def func4():
    return 13.45


def func5():
    return 66


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
