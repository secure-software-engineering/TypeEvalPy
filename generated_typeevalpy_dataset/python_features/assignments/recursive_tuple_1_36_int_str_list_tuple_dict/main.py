# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 36


def func2():
    return 'tjfgq'


def func3():
    return [96, 70, 62]


def func4():
    return (30, 24, 94)


def func5():
    return {'gjpln': 2, 'qsgav': 11, 'qpqhw': 14}


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
