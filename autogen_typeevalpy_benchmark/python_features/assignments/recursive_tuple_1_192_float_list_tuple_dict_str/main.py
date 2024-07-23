# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 15.62


def func2():
    return [10, 88, 74]


def func3():
    return (71, 2, 23)


def func4():
    return {'vlhub': 43, 'syefu': 69, 'sumjn': 12}


def func5():
    return 'vavgs'


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
