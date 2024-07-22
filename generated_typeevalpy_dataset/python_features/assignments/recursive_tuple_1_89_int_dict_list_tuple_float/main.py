# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 41


def func2():
    return {'gkpvr': 100, 'fmjbr': 84, 'xkzba': 33}


def func3():
    return [92, 7, 74]


def func4():
    return (85, 43, 9)


def func5():
    return 62.85


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
