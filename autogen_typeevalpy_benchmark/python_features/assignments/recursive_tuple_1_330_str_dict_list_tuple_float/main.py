# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'buthe'


def func2():
    return {'tinvn': 3, 'nmpuj': 80, 'ceuog': 99}


def func3():
    return [12, 9, 21]


def func4():
    return (19, 44, 21)


def func5():
    return 52.69


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
