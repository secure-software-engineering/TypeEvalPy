# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (69, 76, 49)


def func2():
    return 36


def func3():
    return 69.96


def func4():
    return [74, 45, 39]


def func5():
    return 'viugl'


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
