# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'rfztj'


def func2():
    return {'iktcn': 100, 'vfequ': 64, 'tbzfr': 72}


def func3():
    return (99, 59, 50)


def func4():
    return 42


def func5():
    return 64.61


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
