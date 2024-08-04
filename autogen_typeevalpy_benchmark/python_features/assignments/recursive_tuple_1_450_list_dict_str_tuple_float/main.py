# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [97, 8, 12]


def func2():
    return {'djaem': 57, 'uzril': 7, 'tbjyw': 73}


def func3():
    return 'dbmvp'


def func4():
    return (88, 2, 1)


def func5():
    return 95.74


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
