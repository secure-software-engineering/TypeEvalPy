# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 62


def func2():
    return 'zwipq'


def func3():
    return [67, 99, 69]


def func4():
    return {'jokac': 8, 'qzfkf': 80, 'jptwn': 31}


def func5():
    return (13, 49, 84)


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
