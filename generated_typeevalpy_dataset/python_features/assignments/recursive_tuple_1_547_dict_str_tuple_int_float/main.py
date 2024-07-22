# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'gwnfq': 79, 'pvepj': 40, 'olhqb': 27}


def func2():
    return 'gjbfr'


def func3():
    return (76, 69, 57)


def func4():
    return 61


def func5():
    return 23.82


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
