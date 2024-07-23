# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'lciio': 33, 'lblrn': 29, 'brpka': 9}


def func2():
    return 61.94


def func3():
    return (57, 85, 92)


def func4():
    return 'dytbr'


def func5():
    return [36, 61, 35]


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
