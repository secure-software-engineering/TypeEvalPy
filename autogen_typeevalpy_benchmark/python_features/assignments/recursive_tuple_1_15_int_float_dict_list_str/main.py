# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 44


def func2():
    return 54.56


def func3():
    return {'yxtqw': 7, 'souso': 73, 'dofqo': 67}


def func4():
    return [25, 97, 61]


def func5():
    return 'narnz'


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
