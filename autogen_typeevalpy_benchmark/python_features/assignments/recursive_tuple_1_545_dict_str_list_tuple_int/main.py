# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'jckbo': 12, 'lrdnh': 56, 'selsh': 42}


def func2():
    return 'vhqqd'


def func3():
    return [18, 65, 30]


def func4():
    return (49, 71, 51)


def func5():
    return 91


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
