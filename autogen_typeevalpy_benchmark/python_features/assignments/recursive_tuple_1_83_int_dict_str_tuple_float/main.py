# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 82


def func2():
    return {'ddkhe': 8, 'dafwj': 66, 'nszfl': 55}


def func3():
    return 'qhhhj'


def func4():
    return (54, 32, 41)


def func5():
    return 89.62


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
