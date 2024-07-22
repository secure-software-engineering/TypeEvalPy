# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'nveum': 37, 'rldwe': 6, 'bdekc': 62}


def func2():
    return 3.24


def func3():
    return 'bduig'


def func4():
    return [45, 36, 14]


def func5():
    return (53, 87, 86)


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
