# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 23


def func2():
    return 'fgewg'


def func3():
    return [26, 3, 23]


def func4():
    return 84.45


def func5():
    return (13, 3, 87)


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
