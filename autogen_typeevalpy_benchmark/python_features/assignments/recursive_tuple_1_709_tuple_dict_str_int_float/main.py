# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (29, 37, 3)


def func2():
    return {'ghmbi': 23, 'vbzxy': 57, 'jsqxs': 33}


def func3():
    return 'uvwja'


def func4():
    return 17


def func5():
    return 62.42


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
