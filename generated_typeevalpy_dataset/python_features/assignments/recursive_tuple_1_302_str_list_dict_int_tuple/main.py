# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'cvssu'


def func2():
    return [95, 21, 90]


def func3():
    return {'dgivi': 78, 'qhcps': 93, 'rsede': 49}


def func4():
    return 49


def func5():
    return (89, 17, 100)


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
