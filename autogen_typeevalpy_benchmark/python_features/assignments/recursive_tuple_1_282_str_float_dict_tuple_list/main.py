# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'niood'


def func2():
    return 14.86


def func3():
    return {'xrwbl': 50, 'bauoy': 85, 'dyokm': 56}


def func4():
    return (51, 85, 51)


def func5():
    return [19, 19, 94]


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
