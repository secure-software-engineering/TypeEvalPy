# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 70.94


def func2():
    return 'ytxlp'


def func3():
    return (40, 18, 43)


def func4():
    return {'uwqqq': 80, 'fymlf': 44, 'ncfty': 97}


def func5():
    return [83, 59, 26]


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
