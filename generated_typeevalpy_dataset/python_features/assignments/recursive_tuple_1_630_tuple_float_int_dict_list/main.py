# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (10, 43, 85)


def func2():
    return 21.36


def func3():
    return 7


def func4():
    return {'qsbgb': 90, 'fqtza': 35, 'ssnqj': 41}


def func5():
    return [10, 88, 23]


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
