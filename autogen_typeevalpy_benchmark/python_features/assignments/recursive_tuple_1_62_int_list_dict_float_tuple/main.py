# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 67


def func2():
    return [74, 92, 65]


def func3():
    return {'amcvz': 14, 'zmxym': 56, 'ogeys': 92}


def func4():
    return 3.89


def func5():
    return (42, 50, 99)


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
