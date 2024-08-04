# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 4.98


def func2():
    return {'pocev': 41, 'bxnbf': 82, 'ppmnu': 10}


def func3():
    return (26, 62, 15)


def func4():
    return 57


def func5():
    return 'cfofm'


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
