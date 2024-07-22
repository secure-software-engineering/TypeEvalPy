# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 27.93


def func2():
    return [53, 96, 52]


def func3():
    return 'juosy'


def func4():
    return {'btlfs': 37, 'iptqo': 20, 'ausrs': 55}


def func5():
    return 100


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
