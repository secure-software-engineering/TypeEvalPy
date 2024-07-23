# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'stosv': 9, 'ninlh': 17, 'cdcwv': 86}


def func2():
    return (36, 65, 74)


def func3():
    return [58, 71, 54]


def func4():
    return 'ccdvc'


def func5():
    return 46.41


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
