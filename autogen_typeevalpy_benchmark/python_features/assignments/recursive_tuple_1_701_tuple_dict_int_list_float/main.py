# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (91, 60, 75)


def func2():
    return {'oshnx': 44, 'lpnzp': 56, 'zaczs': 58}


def func3():
    return 45


def func4():
    return [85, 52, 27]


def func5():
    return 37.2


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
