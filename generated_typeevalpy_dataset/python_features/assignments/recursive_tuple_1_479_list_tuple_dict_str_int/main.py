# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [24, 32, 98]


def func2():
    return (93, 29, 95)


def func3():
    return {'zlcsp': 76, 'wfomt': 40, 'iirod': 89}


def func4():
    return 'xabpt'


def func5():
    return 29


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