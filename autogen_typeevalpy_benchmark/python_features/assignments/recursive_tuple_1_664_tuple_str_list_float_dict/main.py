# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (13, 35, 21)


def func2():
    return 'htaza'


def func3():
    return [61, 32, 71]


def func4():
    return 95.43


def func5():
    return {'pfhjn': 95, 'xaiyl': 61, 'wuree': 41}


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
