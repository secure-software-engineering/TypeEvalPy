# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 96


def func2():
    return (41, 35, 76)


def func3():
    return {'idqbo': 28, 'hclje': 40, 'tagpj': 27}


def func4():
    return [73, 56, 11]


def func5():
    return 'lmnlt'


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
