# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (80, 37, 92)


def func2():
    return {'ygcit': 71, 'unxyg': 5, 'mkltq': 23}


def func3():
    return 9.42


def func4():
    return 'nopaf'


def func5():
    return [45, 64, 72]


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
