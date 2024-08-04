# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'pxqoo': 96, 'ikxkl': 29, 'higxy': 40}


def func2():
    return 91


def func3():
    return [33, 10, 40]


def func4():
    return 61.59


def func5():
    return (51, 73, 78)


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
