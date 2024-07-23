# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 20.2


def func2():
    return {'btimb': 67, 'bsamu': 57, 'xrvyv': 77}


def func3():
    return (19, 7, 87)


def func4():
    return [14, 67, 85]


def func5():
    return 'xhnpu'


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
