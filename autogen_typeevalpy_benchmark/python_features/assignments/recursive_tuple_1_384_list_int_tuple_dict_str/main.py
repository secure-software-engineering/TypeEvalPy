# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [56, 65, 64]


def func2():
    return 92


def func3():
    return (20, 17, 41)


def func4():
    return {'nfzaq': 47, 'inkeq': 97, 'gbhax': 50}


def func5():
    return 'jqroa'


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
