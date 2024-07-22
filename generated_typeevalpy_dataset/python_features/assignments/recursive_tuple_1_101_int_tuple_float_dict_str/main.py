# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 13


def func2():
    return (96, 87, 70)


def func3():
    return 46.71


def func4():
    return {'glygb': 47, 'wrkps': 29, 'nvbpe': 4}


def func5():
    return 'jnclj'


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
