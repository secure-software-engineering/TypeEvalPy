# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 9


def func2():
    return 'phicv'


def func3():
    return {'pjypo': 8, 'cytvj': 80, 'juypb': 22}


def func4():
    return 1.1


def func5():
    return (36, 47, 88)


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
