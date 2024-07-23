# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [9, 35, 99]


def func2():
    return 50.02


def func3():
    return (71, 46, 64)


def func4():
    return 'bredj'


def func5():
    return {'iqjze': 43, 'ljwxi': 5, 'gaelo': 46}


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
