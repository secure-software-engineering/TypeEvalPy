# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 95


def func2():
    return [84, 2, 47]


def func3():
    return (93, 74, 14)


def func4():
    return 68.15


def func5():
    return {'zdylv': 52, 'yczeb': 32, 'zqpzq': 5}


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
