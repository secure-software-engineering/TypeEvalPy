# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 97.95


def func2():
    return [22, 30, 35]


def func3():
    return 80


def func4():
    return (73, 79, 44)


def func5():
    return 'qcwjy'


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
