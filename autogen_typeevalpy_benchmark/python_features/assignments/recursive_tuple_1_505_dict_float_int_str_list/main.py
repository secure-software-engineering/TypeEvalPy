# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'sdgge': 45, 'oyucc': 89, 'zdlng': 71}


def func2():
    return 42.18


def func3():
    return 96


def func4():
    return 'prxxl'


def func5():
    return [7, 63, 38]


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
