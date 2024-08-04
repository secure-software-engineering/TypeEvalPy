# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 3.82


def func2():
    return (4, 43, 4)


def func3():
    return 'xawxb'


def func4():
    return {'jpnea': 82, 'xczcm': 1, 'zwndp': 40}


def func5():
    return 61


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
