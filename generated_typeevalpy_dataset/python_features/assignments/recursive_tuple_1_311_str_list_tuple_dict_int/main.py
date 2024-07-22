# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'pxwxj'


def func2():
    return [29, 27, 72]


def func3():
    return (22, 34, 39)


def func4():
    return {'yawyu': 60, 'mqaks': 72, 'dsycx': 28}


def func5():
    return 72


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
