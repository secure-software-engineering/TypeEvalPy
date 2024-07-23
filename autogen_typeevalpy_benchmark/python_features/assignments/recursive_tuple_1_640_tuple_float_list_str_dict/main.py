# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (35, 41, 33)


def func2():
    return 4.15


def func3():
    return [93, 1, 60]


def func4():
    return 'lsmnm'


def func5():
    return {'fusrk': 77, 'riffx': 13, 'pdrty': 36}


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
