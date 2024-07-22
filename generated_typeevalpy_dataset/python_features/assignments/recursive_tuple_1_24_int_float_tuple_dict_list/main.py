# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 84


def func2():
    return 65.81


def func3():
    return (6, 27, 8)


def func4():
    return {'ivvrs': 82, 'iwybs': 9, 'euwne': 7}


def func5():
    return [40, 36, 35]


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
