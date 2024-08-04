# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 86.82


def func2():
    return 'xxjko'


def func3():
    return {'sdxxp': 62, 'qzbtj': 90, 'lklvh': 18}


def func4():
    return (94, 24, 93)


def func5():
    return [99, 76, 66]


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
