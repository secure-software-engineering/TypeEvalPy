# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [41, 40, 28]


def func2():
    return (92, 8, 58)


def func3():
    return {'ofufy': 48, 'ranrd': 94, 'yvxdd': 71}


def func4():
    return 'lxoif'


def func5():
    return 85


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
