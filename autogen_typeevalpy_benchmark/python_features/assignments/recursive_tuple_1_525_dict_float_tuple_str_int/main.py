# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'uosab': 79, 'dvfim': 53, 'diizd': 60}


def func2():
    return 84.29


def func3():
    return (72, 51, 87)


def func4():
    return 'nvsqz'


def func5():
    return 34


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
