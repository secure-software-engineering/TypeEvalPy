# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (40, 49, 52)


def func2():
    return 43.45


def func3():
    return 30


def func4():
    return {'abuvz': 47, 'rldby': 11, 'vvuyw': 46}


def func5():
    return [60, 18, 68]


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
