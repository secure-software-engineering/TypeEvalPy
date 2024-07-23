# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ockti': 8, 'dmkzi': 6, 'sqxxh': 35}


def func2():
    return 74


def func3():
    return [100, 39, 80]


def func4():
    return (46, 26, 74)


def func5():
    return 44.92


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
