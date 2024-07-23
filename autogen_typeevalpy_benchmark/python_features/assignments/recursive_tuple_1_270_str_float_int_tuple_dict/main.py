# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'dekou'


def func2():
    return 87.27


def func3():
    return 79


def func4():
    return (84, 87, 52)


def func5():
    return {'przhw': 88, 'binwy': 13, 'iilus': 50}


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
