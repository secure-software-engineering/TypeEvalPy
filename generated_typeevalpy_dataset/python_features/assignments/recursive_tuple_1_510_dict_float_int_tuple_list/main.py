# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'sncgg': 30, 'wfcgt': 14, 'edzpa': 25}


def func2():
    return 17.76


def func3():
    return 45


def func4():
    return (83, 41, 25)


def func5():
    return [69, 33, 46]


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
