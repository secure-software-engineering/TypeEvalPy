# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 43


def func2():
    return [43, 22, 11]


def func3():
    return 'cfygm'


def func4():
    return (23, 90, 95)


def func5():
    return {'qtdyk': 50, 'swfuq': 97, 'jjtpx': 54}


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
