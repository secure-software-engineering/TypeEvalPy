# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (26, 96, 81)


def func2():
    return [71, 29, 42]


def func3():
    return {'hyhon': 97, 'lrauk': 98, 'nhmqq': 70}


def func4():
    return 85


def func5():
    return 8.64


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
