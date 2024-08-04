# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (37, 74, 58)


def func2():
    return 27.46


def func3():
    return {'pqfnf': 91, 'purtv': 65, 'svpcp': 55}


def func4():
    return [5, 76, 95]


def func5():
    return 'qiiwp'


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
