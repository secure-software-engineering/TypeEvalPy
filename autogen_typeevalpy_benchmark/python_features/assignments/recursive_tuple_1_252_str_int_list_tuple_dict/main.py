# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'hnaqd'


def func2():
    return 16


def func3():
    return [71, 14, 51]


def func4():
    return (84, 28, 46)


def func5():
    return {'nwnwe': 80, 'crkxu': 85, 'ejxun': 79}


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
