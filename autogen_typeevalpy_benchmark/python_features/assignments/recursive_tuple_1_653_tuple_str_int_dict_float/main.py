# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (72, 10, 24)


def func2():
    return 'gyfkw'


def func3():
    return 44


def func4():
    return {'cempa': 83, 'pqinj': 82, 'itzcm': 42}


def func5():
    return 56.27


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
