# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [41, 55, 47]


def func2():
    return 'mlnal'


def func3():
    return (40, 99, 41)


def func4():
    return {'zenpl': 14, 'gugkj': 51, 'dquih': 81}


def func5():
    return 43


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
