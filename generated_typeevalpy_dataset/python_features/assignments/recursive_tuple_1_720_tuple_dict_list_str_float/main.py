# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (47, 52, 69)


def func2():
    return {'vhvwn': 42, 'itpvy': 42, 'anxzi': 9}


def func3():
    return [22, 82, 13]


def func4():
    return 'mdkhz'


def func5():
    return 50.86


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