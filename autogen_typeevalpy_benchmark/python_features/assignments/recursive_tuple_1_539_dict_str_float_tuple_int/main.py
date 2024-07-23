# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'gafpx': 91, 'drien': 47, 'flcuw': 34}


def func2():
    return 'ncxzc'


def func3():
    return 28.72


def func4():
    return (68, 69, 89)


def func5():
    return 43


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
