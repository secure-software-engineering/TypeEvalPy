# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'cfjfq': 19, 'dhmcp': 60, 'jabzy': 63}


def func2():
    return (85, 5, 42)


def func3():
    return 'kkytv'


def func4():
    return [8, 61, 56]


def func5():
    return 87.16


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
