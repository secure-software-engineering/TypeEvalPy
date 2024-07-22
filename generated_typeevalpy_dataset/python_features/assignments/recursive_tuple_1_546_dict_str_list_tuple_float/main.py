# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'gewem': 55, 'fbxzo': 43, 'vsdpq': 20}


def func2():
    return 'kdkfy'


def func3():
    return [93, 26, 24]


def func4():
    return (23, 26, 28)


def func5():
    return 27.57


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
