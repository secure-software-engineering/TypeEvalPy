# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'dohae'


def func2():
    return 80.24


def func3():
    return [48, 49, 82]


def func4():
    return (80, 14, 39)


def func5():
    return {'hbkkj': 96, 'oefgd': 7, 'iklmc': 55}


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
