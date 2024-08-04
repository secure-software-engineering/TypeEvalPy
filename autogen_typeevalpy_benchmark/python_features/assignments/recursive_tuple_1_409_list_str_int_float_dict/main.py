# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [80, 8, 57]


def func2():
    return 'szlwa'


def func3():
    return 30


def func4():
    return 13.87


def func5():
    return {'wnyci': 47, 'yewqa': 52, 'swaba': 64}


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
