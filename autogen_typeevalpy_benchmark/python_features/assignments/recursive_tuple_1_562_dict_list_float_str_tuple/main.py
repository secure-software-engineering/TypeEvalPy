# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'rdyvc': 3, 'yamfd': 38, 'yyxvh': 32}


def func2():
    return [12, 7, 70]


def func3():
    return 39.99


def func4():
    return 'mynja'


def func5():
    return (84, 74, 56)


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
