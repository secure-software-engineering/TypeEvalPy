# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'kydub'


def func2():
    return 1


def func3():
    return [13, 55, 12]


def func4():
    return (85, 27, 83)


def func5():
    return 37.19


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
