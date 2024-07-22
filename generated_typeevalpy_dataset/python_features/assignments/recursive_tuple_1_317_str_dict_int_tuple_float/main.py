# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'avyqq'


def func2():
    return {'jrfab': 69, 'kiahx': 31, 'utxpi': 16}


def func3():
    return 46


def func4():
    return (77, 3, 95)


def func5():
    return 24.76


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
