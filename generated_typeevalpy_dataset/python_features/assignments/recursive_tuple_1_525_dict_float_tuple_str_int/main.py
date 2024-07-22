# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'bvvnk': 7, 'otmit': 69, 'amjhk': 22}


def func2():
    return 4.17


def func3():
    return (49, 7, 3)


def func4():
    return 'arqts'


def func5():
    return 19


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
