# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (80, 71, 76)


def func2():
    return 'vyygl'


def func3():
    return [19, 29, 84]


def func4():
    return 47.9


def func5():
    return 58


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
