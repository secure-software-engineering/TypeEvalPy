# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'uytck'


def func2():
    return (99, 55, 69)


def func3():
    return [69, 60, 67]


def func4():
    return 89.32


def func5():
    return {'xomwu': 27, 'tlycl': 50, 'efibs': 46}


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
