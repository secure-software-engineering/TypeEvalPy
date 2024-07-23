# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 28.45


def func2():
    return 9


def func3():
    return (49, 60, 75)


def func4():
    return [83, 24, 3]


def func5():
    return {'mbxsm': 39, 'xpofl': 81, 'oqucf': 31}


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
