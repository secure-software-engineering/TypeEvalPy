# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 60.76


def func2():
    return {'uljmi': 76, 'njuzn': 34, 'jrdiy': 26}


def func3():
    return 66


def func4():
    return [79, 94, 59]


def func5():
    return (56, 7, 60)


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
