# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'uljwo': 72, 'gbuwm': 80, 'avffa': 100}


def func2():
    return (49, 83, 72)


def func3():
    return [33, 60, 25]


def func4():
    return 'aehcq'


def func5():
    return 62


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
