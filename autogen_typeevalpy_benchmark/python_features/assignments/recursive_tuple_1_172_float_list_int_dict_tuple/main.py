# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 54.03


def func2():
    return [92, 30, 38]


def func3():
    return 21


def func4():
    return {'xifty': 32, 'aayck': 5, 'mehfu': 35}


def func5():
    return (96, 16, 49)


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
