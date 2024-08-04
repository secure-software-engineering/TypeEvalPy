# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 21


def func2():
    return (90, 56, 46)


def func3():
    return 'xovox'


def func4():
    return {'fspdr': 87, 'vtvta': 53, 'xymiu': 34}


def func5():
    return [67, 93, 1]


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
