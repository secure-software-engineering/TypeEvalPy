# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 72


def func2():
    return [33, 97, 5]


def func3():
    return (11, 16, 65)


def func4():
    return {'hzezr': 46, 'gbyxh': 78, 'ndmix': 69}


def func5():
    return 'nrrba'


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
