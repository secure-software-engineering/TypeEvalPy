# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [80, 93, 66]


def func2():
    return {'yzfin': 9, 'fuuai': 60, 'durkr': 38}


def func3():
    return (28, 94, 47)


def func4():
    return 57


def func5():
    return 'gtvix'


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
