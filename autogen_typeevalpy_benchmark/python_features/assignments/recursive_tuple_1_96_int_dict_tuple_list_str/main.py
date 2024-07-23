# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 45


def func2():
    return {'ceutz': 25, 'kevno': 32, 'tlpex': 87}


def func3():
    return (19, 79, 44)


def func4():
    return [80, 21, 60]


def func5():
    return 'flbdk'


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
