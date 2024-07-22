# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 33


def func2():
    return 'xrmhl'


def func3():
    return 45.44


def func4():
    return [20, 82, 45]


def func5():
    return {'brabu': 70, 'gfzmc': 25, 'kutmw': 48}


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
