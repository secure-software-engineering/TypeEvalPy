# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 90.52


def func2():
    return 'pnrxt'


def func3():
    return [81, 6, 81]


def func4():
    return 93


def func5():
    return (1, 49, 98)


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
