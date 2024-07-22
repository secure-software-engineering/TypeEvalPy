# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 4.75


def func2():
    return (29, 5, 67)


def func3():
    return [48, 84, 1]


def func4():
    return 'zxvpp'


def func5():
    return 59


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
