# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 87.53


def func2():
    return 'cdfkv'


def func3():
    return [51, 85, 46]


def func4():
    return {'gixiw': 100, 'luaax': 10, 'stldf': 22}


def func5():
    return 80


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
