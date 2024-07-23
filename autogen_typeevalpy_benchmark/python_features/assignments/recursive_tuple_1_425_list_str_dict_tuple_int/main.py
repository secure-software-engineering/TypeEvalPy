# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [20, 89, 79]


def func2():
    return 'zohhg'


def func3():
    return {'cgpcg': 45, 'fuadi': 86, 'knmzr': 87}


def func4():
    return (84, 70, 25)


def func5():
    return 31


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
