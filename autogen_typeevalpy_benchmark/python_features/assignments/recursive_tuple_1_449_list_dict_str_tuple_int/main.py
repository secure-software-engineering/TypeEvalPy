# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [23, 65, 21]


def func2():
    return {'xpxxh': 10, 'bmqxn': 50, 'eglcz': 70}


def func3():
    return 'yujmb'


def func4():
    return (45, 72, 83)


def func5():
    return 90


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
