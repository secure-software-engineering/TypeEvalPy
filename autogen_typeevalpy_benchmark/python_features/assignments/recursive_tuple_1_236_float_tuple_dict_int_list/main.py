# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 5.06


def func2():
    return (33, 15, 81)


def func3():
    return {'mpwru': 56, 'tfczp': 54, 'pjwrv': 8}


def func4():
    return 82


def func5():
    return [14, 99, 36]


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
