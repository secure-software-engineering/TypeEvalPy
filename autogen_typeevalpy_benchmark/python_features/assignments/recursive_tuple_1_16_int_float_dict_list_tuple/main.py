# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 36


def func2():
    return 78.89


def func3():
    return {'gsxlu': 15, 'pkbwa': 13, 'lkwig': 70}


def func4():
    return [22, 37, 19]


def func5():
    return (24, 33, 99)


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
