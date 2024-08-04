# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 88


def func2():
    return {'grizt': 90, 'lhmtg': 32, 'dngtw': 86}


def func3():
    return 'vfsvs'


def func4():
    return [65, 79, 24]


def func5():
    return (25, 76, 81)


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
