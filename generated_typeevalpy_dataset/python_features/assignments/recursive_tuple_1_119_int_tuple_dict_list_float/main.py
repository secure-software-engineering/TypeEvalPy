# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 21


def func2():
    return (53, 33, 43)


def func3():
    return {'ieydg': 45, 'njisp': 27, 'erwke': 53}


def func4():
    return [4, 67, 4]


def func5():
    return 53.42


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
