# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'mumwp': 77, 'sokvp': 18, 'hexpo': 69}


def func2():
    return (24, 38, 56)


def func3():
    return 55


def func4():
    return [7, 7, 8]


def func5():
    return 'mcyix'


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
