# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'rmeav': 61, 'ixutu': 1, 'zcevz': 59}


def func2():
    return 'ggbzv'


def func3():
    return (98, 39, 38)


def func4():
    return 17


def func5():
    return [24, 47, 19]


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
