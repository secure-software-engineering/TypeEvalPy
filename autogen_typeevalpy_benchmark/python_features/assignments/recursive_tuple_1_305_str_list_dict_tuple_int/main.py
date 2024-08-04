# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ndpgz'


def func2():
    return [71, 51, 1]


def func3():
    return {'bvgmy': 41, 'ovnkg': 16, 'zqmcl': 18}


def func4():
    return (24, 16, 47)


def func5():
    return 98


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
