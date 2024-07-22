# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 46


def func2():
    return {'dybnh': 87, 'vuczg': 25, 'pdsnt': 57}


def func3():
    return [30, 41, 95]


def func4():
    return 69.8


def func5():
    return (32, 30, 9)


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
