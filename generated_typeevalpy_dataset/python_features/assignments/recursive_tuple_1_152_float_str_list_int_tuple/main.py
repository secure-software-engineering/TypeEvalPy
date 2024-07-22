# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 62.99


def func2():
    return 'gycin'


def func3():
    return [87, 84, 54]


def func4():
    return 90


def func5():
    return (96, 66, 42)


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
