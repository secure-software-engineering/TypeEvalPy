# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (4, 71, 89)


def func2():
    return 55.14


def func3():
    return {'rosve': 64, 'dknru': 72, 'sndpj': 58}


def func4():
    return 'djxfi'


def func5():
    return [84, 25, 20]


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
