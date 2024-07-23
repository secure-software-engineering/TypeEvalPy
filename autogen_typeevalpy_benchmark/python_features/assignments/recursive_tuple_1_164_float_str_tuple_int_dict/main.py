# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 63.92


def func2():
    return 'hdlez'


def func3():
    return (74, 41, 2)


def func4():
    return 8


def func5():
    return {'grygj': 60, 'zpjuf': 11, 'uurcw': 48}


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
