# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'dpbmr': 45, 'yoyvj': 79, 'hbdud': 77}


def func2():
    return 44.18


def func3():
    return (62, 18, 41)


def func4():
    return 'ytewd'


def func5():
    return 2


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
