# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'uzcew': 45, 'kphrw': 15, 'kkdhn': 8}


def func2():
    return 100


def func3():
    return 'dqwgn'


def func4():
    return 10.92


def func5():
    return (83, 43, 64)


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
