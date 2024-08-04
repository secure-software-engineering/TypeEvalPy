# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 35.73


def func2():
    return 70


def func3():
    return [33, 85, 63]


def func4():
    return (33, 47, 59)


def func5():
    return 'ajsxu'


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
