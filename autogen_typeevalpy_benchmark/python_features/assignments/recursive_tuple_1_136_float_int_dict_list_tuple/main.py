# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 38.22


def func2():
    return 56


def func3():
    return {'cnsnr': 39, 'jjmyl': 32, 'xatcd': 75}


def func4():
    return [66, 48, 17]


def func5():
    return (80, 70, 73)


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