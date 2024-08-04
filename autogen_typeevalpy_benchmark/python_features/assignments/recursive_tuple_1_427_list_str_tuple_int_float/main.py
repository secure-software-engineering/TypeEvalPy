# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [51, 81, 49]


def func2():
    return 'yoqnu'


def func3():
    return (32, 90, 75)


def func4():
    return 51


def func5():
    return 69.95


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
