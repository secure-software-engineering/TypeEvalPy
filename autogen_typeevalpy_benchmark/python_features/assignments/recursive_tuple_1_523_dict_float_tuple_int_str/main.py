# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'uqtlf': 61, 'afkeb': 83, 'yeico': 64}


def func2():
    return 45.49


def func3():
    return (45, 24, 5)


def func4():
    return 6


def func5():
    return 'iuitw'


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
