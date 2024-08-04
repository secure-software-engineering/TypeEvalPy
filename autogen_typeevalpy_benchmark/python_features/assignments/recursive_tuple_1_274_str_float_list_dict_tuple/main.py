# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ldtka'


def func2():
    return 14.8


def func3():
    return [41, 49, 81]


def func4():
    return {'djlvx': 71, 'dyfam': 36, 'hfmev': 30}


def func5():
    return (25, 63, 78)


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
