# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'kgvnq': 78, 'ftnnz': 22, 'hpaha': 85}


def func2():
    return 64.36


def func3():
    return [51, 2, 42]


def func4():
    return (22, 16, 5)


def func5():
    return 21


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
