# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (95, 16, 79)


def func2():
    return {'htfpx': 54, 'xrzlk': 9, 'lbemx': 17}


def func3():
    return [4, 74, 21]


def func4():
    return 71


def func5():
    return 9.57


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
