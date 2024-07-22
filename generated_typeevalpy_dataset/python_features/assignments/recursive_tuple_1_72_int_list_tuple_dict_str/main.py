# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 18


def func2():
    return [69, 83, 90]


def func3():
    return (70, 23, 13)


def func4():
    return {'sieun': 96, 'ylqag': 15, 'bphpx': 69}


def func5():
    return 'yacgv'


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
