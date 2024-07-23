# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 93.27


def func2():
    return {'goqpj': 4, 'copmj': 49, 'xqpay': 92}


def func3():
    return 49


def func4():
    return [45, 13, 51]


def func5():
    return 'kevku'


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
