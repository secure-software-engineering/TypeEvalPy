# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'hyjgm'


def func2():
    return {'fclpl': 68, 'pasom': 31, 'lsfbb': 22}


def func3():
    return [25, 45, 23]


def func4():
    return (72, 17, 69)


def func5():
    return 42.5


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
