# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 19.03


def func2():
    return {'crtha': 71, 'qxnsf': 51, 'tifyg': 33}


def func3():
    return 41


def func4():
    return [54, 57, 35]


def func5():
    return 'pgbxa'


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
