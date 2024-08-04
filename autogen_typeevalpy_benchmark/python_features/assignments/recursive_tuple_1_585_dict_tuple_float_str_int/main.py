# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'xjffa': 29, 'ejbvx': 44, 'uizcx': 37}


def func2():
    return (43, 92, 88)


def func3():
    return 89.85


def func4():
    return 'fknoo'


def func5():
    return 89


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
