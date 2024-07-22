# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'oeacp': 84, 'yymwh': 39, 'oryts': 5}


def func2():
    return (36, 48, 43)


def func3():
    return 50


def func4():
    return 48.12


def func5():
    return 'esnon'


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
