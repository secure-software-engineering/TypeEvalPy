# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [52, 4, 24]


def func2():
    return 'nyqex'


def func3():
    return (37, 3, 38)


def func4():
    return 95.71


def func5():
    return {'dyovl': 80, 'fpxqq': 100, 'atitz': 64}


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
