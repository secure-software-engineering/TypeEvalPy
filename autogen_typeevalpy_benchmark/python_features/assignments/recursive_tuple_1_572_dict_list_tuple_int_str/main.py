# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'qlftn': 95, 'shmmp': 63, 'cskrz': 24}


def func2():
    return [99, 57, 64]


def func3():
    return (61, 10, 55)


def func4():
    return 95


def func5():
    return 'dkjqr'


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
