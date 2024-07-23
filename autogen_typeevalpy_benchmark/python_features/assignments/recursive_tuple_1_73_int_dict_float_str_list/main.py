# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 92


def func2():
    return {'mjfai': 35, 'mwvbz': 10, 'ikcae': 87}


def func3():
    return 74.0


def func4():
    return 'sbdun'


def func5():
    return [66, 72, 8]


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
