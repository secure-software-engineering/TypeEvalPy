# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'lktxm'


def func2():
    return 60.08


def func3():
    return (86, 32, 10)


def func4():
    return [79, 14, 1]


def func5():
    return {'wqwyy': 54, 'hjoeb': 84, 'felwb': 3}


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
