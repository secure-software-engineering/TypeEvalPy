# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 67


def func2():
    return 74.01


def func3():
    return [14, 42, 67]


def func4():
    return (75, 25, 100)


def func5():
    return 'jcsvc'


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
