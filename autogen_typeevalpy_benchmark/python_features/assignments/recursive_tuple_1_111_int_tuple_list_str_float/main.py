# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 24


def func2():
    return (55, 74, 41)


def func3():
    return [17, 65, 99]


def func4():
    return 'uvorz'


def func5():
    return 30.81


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
