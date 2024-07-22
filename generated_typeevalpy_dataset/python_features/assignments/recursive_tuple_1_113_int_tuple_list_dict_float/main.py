# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 95


def func2():
    return (35, 50, 98)


def func3():
    return [27, 18, 38]


def func4():
    return {'uvfwq': 49, 'skack': 89, 'uesap': 79}


def func5():
    return 64.38


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
