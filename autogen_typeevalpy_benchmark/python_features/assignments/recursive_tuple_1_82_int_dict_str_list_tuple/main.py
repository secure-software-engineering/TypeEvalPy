# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 59


def func2():
    return {'sewtf': 64, 'agbpt': 37, 'pcagi': 89}


def func3():
    return 'iuiyg'


def func4():
    return [66, 2, 1]


def func5():
    return (30, 83, 1)


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
