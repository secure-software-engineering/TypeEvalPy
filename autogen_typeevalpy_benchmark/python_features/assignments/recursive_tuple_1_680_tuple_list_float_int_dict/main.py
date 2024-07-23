# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (51, 36, 53)


def func2():
    return [70, 71, 7]


def func3():
    return 36.19


def func4():
    return 69


def func5():
    return {'mkrgl': 2, 'wbaqo': 94, 'jddop': 53}


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
