# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'reada'


def func2():
    return {'avtqh': 84, 'nizew': 34, 'kczxm': 41}


def func3():
    return (97, 9, 4)


def func4():
    return 46.79


def func5():
    return [13, 84, 81]


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
