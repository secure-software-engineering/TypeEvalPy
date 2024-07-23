# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 31


def func2():
    return 67.08


def func3():
    return {'bebyv': 92, 'vzdhx': 27, 'pmsuf': 70}


def func4():
    return (73, 56, 72)


def func5():
    return [48, 46, 63]


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
