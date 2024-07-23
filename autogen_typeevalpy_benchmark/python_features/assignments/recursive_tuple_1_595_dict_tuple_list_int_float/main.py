# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'csqby': 97, 'lgedp': 92, 'fitpg': 86}


def func2():
    return (68, 64, 52)


def func3():
    return [59, 33, 43]


def func4():
    return 26


def func5():
    return 99.77


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
