# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (54, 62, 38)


def func2():
    return 'yfwls'


def func3():
    return [50, 52, 24]


def func4():
    return 76


def func5():
    return {'fzxcc': 73, 'vyuco': 40, 'duxvv': 54}


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
