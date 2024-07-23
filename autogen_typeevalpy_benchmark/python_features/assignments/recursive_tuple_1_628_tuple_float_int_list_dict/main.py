# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (65, 41, 50)


def func2():
    return 38.05


def func3():
    return 70


def func4():
    return [55, 99, 47]


def func5():
    return {'mgctp': 21, 'ljavj': 95, 'yqssi': 32}


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
