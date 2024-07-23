# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [6, 20, 22]


def func2():
    return (21, 9, 30)


def func3():
    return {'unlyf': 72, 'drwyz': 77, 'okgar': 15}


def func4():
    return 33


def func5():
    return 'zbbxq'


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
