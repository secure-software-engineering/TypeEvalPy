# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'pgawo': 20, 'kbkwb': 89, 'souws': 75}


def func2():
    return 90


def func3():
    return 89.74


def func4():
    return [95, 97, 40]


def func5():
    return (71, 47, 94)


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
