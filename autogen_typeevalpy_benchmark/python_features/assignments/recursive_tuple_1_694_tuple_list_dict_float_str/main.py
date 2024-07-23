# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (46, 11, 35)


def func2():
    return [1, 63, 35]


def func3():
    return {'gwyqo': 42, 'dtrnv': 11, 'frhqr': 14}


def func4():
    return 74.82


def func5():
    return 'wmqyo'


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
