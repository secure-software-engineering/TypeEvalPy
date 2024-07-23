# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 83.99


def func2():
    return 'foefo'


def func3():
    return {'rmdho': 48, 'vekqi': 51, 'bjffi': 80}


def func4():
    return [51, 18, 23]


def func5():
    return 49


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
