# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'yuvux': 34, 'aleeu': 85, 'hwbvs': 70}


def func2():
    return 60


def func3():
    return (94, 100, 14)


def func4():
    return [61, 83, 82]


def func5():
    return 69.41


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
