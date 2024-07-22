# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'lxytu'


def func2():
    return 6


def func3():
    return (73, 87, 42)


def func4():
    return {'ssjvm': 74, 'iwjhe': 78, 'rcnvf': 67}


def func5():
    return [66, 83, 8]


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
