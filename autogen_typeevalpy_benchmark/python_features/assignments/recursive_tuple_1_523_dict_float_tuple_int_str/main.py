# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'cjzgd': 100, 'yuxbf': 77, 'rstkp': 46}


def func2():
    return 64.86


def func3():
    return (3, 46, 50)


def func4():
    return 38


def func5():
    return 'cgovz'


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
