# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [91, 93, 94]


def func2():
    return {'rwdgo': 63, 'zspfx': 87, 'emzsd': 6}


def func3():
    return (71, 31, 35)


def func4():
    return 'xiilq'


def func5():
    return 41.74


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
