# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'dqorq'


def func2():
    return 33.76


def func3():
    return {'gansm': 52, 'acogr': 34, 'jplps': 41}


def func4():
    return (38, 47, 7)


def func5():
    return 60


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
