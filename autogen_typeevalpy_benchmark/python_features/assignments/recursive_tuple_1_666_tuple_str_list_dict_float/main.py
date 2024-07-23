# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (53, 49, 14)


def func2():
    return 'rdxbd'


def func3():
    return [40, 57, 92]


def func4():
    return {'zlqvu': 55, 'mrspr': 63, 'iwntb': 55}


def func5():
    return 56.72


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
