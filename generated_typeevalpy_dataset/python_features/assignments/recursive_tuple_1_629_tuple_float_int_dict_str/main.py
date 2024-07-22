# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (49, 59, 20)


def func2():
    return 37.41


def func3():
    return 91


def func4():
    return {'zzosr': 38, 'elaao': 30, 'ossij': 56}


def func5():
    return 'quhtg'


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
