# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 86


def func2():
    return 27.74


def func3():
    return (86, 35, 39)


def func4():
    return 'ggmaf'


def func5():
    return {'ypsca': 39, 'flyjq': 50, 'ffufw': 18}


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
