# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'yxrgv': 60, 'ertjx': 78, 'bmutp': 6}


def func2():
    return [52, 14, 8]


def func3():
    return 'cqefk'


def func4():
    return 80


def func5():
    return (82, 49, 99)


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
