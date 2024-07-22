# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'pifwq'


def func2():
    return 60.85


def func3():
    return [80, 15, 55]


def func4():
    return {'wqflb': 92, 'wguhc': 12, 'inaha': 57}


def func5():
    return 29


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
