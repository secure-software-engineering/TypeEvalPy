# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (30, 50, 83)


def func2():
    return 5


def func3():
    return {'kczpl': 85, 'pxxgq': 11, 'fohnq': 13}


def func4():
    return 86.86


def func5():
    return 'hpfpw'


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
