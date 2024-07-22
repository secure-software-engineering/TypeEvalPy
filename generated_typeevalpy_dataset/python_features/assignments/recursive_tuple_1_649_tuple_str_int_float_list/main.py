# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (99, 11, 22)


def func2():
    return 'bpjwh'


def func3():
    return 1


def func4():
    return 63.59


def func5():
    return [59, 1, 44]


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
