# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 47


def func2():
    return (29, 96, 56)


def func3():
    return 56.58


def func4():
    return {'rkblj': 77, 'sivvm': 82, 'kaycb': 6}


def func5():
    return [85, 9, 48]


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
