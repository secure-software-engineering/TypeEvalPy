# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'bgbdk'


def func2():
    return (68, 16, 72)


def func3():
    return {'xtgtz': 32, 'qomwg': 20, 'fseqk': 87}


def func4():
    return 9


def func5():
    return 15.01


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
