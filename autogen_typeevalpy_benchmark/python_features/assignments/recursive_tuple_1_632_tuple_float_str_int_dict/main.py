# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (49, 3, 28)


def func2():
    return 76.97


def func3():
    return 'smdfx'


def func4():
    return 87


def func5():
    return {'dxfkc': 69, 'xasxq': 37, 'zwvqy': 31}


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
