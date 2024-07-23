# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 31


def func2():
    return 'gqkxd'


def func3():
    return {'tcrui': 59, 'vbuiv': 89, 'wciir': 7}


def func4():
    return (47, 47, 50)


def func5():
    return [42, 56, 56]


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
