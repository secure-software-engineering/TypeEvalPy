# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 43.6


def func2():
    return (42, 9, 47)


def func3():
    return {'ttnem': 1, 'clikp': 41, 'tydxc': 10}


def func4():
    return 36


def func5():
    return [98, 97, 50]


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
