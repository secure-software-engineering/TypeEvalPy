# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ojsnv'


def func2():
    return 45


def func3():
    return {'sqhbf': 94, 'wilkb': 18, 'kphuf': 64}


def func4():
    return 41.02


def func5():
    return [12, 69, 30]


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
