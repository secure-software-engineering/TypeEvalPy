# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 26.61


def func2():
    return 41


def func3():
    return (82, 18, 28)


def func4():
    return {'fnwgd': 4, 'uhush': 30, 'gwfrj': 34}


def func5():
    return [45, 44, 16]


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
