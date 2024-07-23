# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'bpsis'


def func2():
    return [15, 6, 54]


def func3():
    return {'spems': 7, 'dfnqj': 100, 'fgfek': 99}


def func4():
    return 31


def func5():
    return (74, 32, 53)


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
