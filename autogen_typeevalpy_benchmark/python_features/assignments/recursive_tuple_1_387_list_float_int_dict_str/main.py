# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [50, 22, 74]


def func2():
    return 18.01


def func3():
    return 76


def func4():
    return {'fsipr': 72, 'cwycs': 42, 'jaqny': 3}


def func5():
    return 'ptuhg'


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
