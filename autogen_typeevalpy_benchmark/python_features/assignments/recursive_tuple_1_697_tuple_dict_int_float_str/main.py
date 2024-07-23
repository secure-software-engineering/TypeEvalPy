# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (50, 77, 47)


def func2():
    return {'chqra': 83, 'rbdce': 55, 'pegoz': 18}


def func3():
    return 42


def func4():
    return 9.65


def func5():
    return 'oojtz'


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
