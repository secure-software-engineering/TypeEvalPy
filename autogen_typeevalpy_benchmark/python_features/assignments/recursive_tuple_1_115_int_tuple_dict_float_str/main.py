# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 91


def func2():
    return (3, 5, 28)


def func3():
    return {'iithb': 12, 'gbczp': 49, 'vcglm': 36}


def func4():
    return 81.59


def func5():
    return 'kdjva'


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
