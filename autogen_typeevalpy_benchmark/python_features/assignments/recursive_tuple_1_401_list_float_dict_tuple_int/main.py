# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [90, 69, 91]


def func2():
    return 17.34


def func3():
    return {'ucgrt': 70, 'iqbkf': 6, 'lornv': 17}


def func4():
    return (94, 84, 89)


def func5():
    return 41


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
