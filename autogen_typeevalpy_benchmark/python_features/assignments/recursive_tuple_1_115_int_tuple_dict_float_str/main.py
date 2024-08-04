# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 4


def func2():
    return (80, 91, 70)


def func3():
    return {'xcjtd': 99, 'lqjgx': 34, 'hnguu': 85}


def func4():
    return 6.12


def func5():
    return 'cdazw'


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
