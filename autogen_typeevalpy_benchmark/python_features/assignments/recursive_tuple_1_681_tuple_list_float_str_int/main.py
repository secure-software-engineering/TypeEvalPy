# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (87, 77, 57)


def func2():
    return [14, 38, 63]


def func3():
    return 96.41


def func4():
    return 'zjliz'


def func5():
    return 69


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
