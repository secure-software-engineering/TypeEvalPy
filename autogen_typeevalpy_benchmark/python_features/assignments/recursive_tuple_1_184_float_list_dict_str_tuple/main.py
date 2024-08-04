# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 28.03


def func2():
    return [83, 36, 83]


def func3():
    return {'mbsgq': 14, 'zvwyz': 5, 'qmmwt': 48}


def func4():
    return 'axdtw'


def func5():
    return (17, 11, 54)


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
