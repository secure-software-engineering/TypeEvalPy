# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [5, 38, 54]


def func2():
    return 33.34


def func3():
    return 'tzizd'


def func4():
    return 22


def func5():
    return (55, 70, 4)


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