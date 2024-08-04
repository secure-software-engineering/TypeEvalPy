# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [68, 87, 69]


def func2():
    return 34


def func3():
    return {'bffgy': 22, 'yisei': 87, 'ycoca': 14}


def func4():
    return 'cejfk'


def func5():
    return 82.69


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
