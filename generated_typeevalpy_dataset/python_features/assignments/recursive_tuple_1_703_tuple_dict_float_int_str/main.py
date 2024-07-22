# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (46, 4, 89)


def func2():
    return {'rpgyp': 7, 'bsfds': 23, 'hawpm': 23}


def func3():
    return 22.63


def func4():
    return 16


def func5():
    return 'ucnkc'


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
