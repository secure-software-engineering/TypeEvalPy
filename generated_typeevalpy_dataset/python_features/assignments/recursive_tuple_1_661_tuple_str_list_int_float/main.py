# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (26, 79, 18)


def func2():
    return 'qvujk'


def func3():
    return [55, 61, 50]


def func4():
    return 82


def func5():
    return 40.64


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
