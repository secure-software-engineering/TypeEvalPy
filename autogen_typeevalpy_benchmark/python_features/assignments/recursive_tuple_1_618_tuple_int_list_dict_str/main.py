# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (53, 73, 80)


def func2():
    return 17


def func3():
    return [2, 50, 54]


def func4():
    return {'kzyok': 94, 'eippx': 71, 'pvptu': 32}


def func5():
    return 'fttwk'


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
