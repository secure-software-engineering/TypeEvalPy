# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (55, 83, 81)


def func2():
    return {'slbga': 100, 'yrorl': 8, 'rzotv': 37}


def func3():
    return [66, 86, 89]


def func4():
    return 17.35


def func5():
    return 14


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
