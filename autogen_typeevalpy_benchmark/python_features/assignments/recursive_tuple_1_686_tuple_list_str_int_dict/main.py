# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (25, 12, 65)


def func2():
    return [11, 13, 45]


def func3():
    return 'xsbsz'


def func4():
    return 89


def func5():
    return {'vudwu': 41, 'donvs': 53, 'mrulg': 75}


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
