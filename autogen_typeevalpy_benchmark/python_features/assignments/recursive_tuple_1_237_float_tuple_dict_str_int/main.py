# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 84.39


def func2():
    return (94, 36, 33)


def func3():
    return {'qirgj': 78, 'asmpf': 73, 'lgzvm': 49}


def func4():
    return 'pwrbc'


def func5():
    return 83


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
