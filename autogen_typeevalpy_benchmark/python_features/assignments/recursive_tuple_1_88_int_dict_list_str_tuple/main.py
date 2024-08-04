# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 35


def func2():
    return {'wbzzf': 38, 'dqqzi': 42, 'ywgdx': 8}


def func3():
    return [81, 2, 46]


def func4():
    return 'fzezn'


def func5():
    return (100, 100, 75)


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
