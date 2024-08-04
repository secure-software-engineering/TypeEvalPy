# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [13, 31, 55]


def func2():
    return 45.29


def func3():
    return 41


def func4():
    return (6, 3, 80)


def func5():
    return {'gwsqc': 8, 'yuajl': 78, 'qydpm': 94}


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
