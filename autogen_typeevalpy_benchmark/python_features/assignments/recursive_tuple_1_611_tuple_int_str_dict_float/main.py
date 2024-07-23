# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (22, 72, 81)


def func2():
    return 3


def func3():
    return 'bxdel'


def func4():
    return {'mqcjh': 39, 'olvmc': 80, 'pnxfo': 64}


def func5():
    return 75.37


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
