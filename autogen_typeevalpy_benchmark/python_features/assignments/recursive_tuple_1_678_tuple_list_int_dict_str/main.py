# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (22, 28, 32)


def func2():
    return [100, 45, 9]


def func3():
    return 59


def func4():
    return {'hkjwd': 83, 'vvcjm': 49, 'dfouj': 79}


def func5():
    return 'qjtqm'


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
