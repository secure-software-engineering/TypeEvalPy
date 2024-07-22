# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'wxcqs'


def func2():
    return 72


def func3():
    return [5, 71, 6]


def func4():
    return 49.41


def func5():
    return (65, 13, 80)


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
