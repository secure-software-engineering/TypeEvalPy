# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (10, 54, 93)


def func2():
    return 51.12


def func3():
    return {'yykhm': 18, 'ylfjg': 81, 'uiiqu': 37}


def func4():
    return 'cvquh'


def func5():
    return [7, 17, 64]


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
