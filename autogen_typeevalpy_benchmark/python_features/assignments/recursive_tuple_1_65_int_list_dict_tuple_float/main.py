# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 10


def func2():
    return [44, 76, 40]


def func3():
    return {'ucdvd': 74, 'rulhg': 86, 'niwud': 96}


def func4():
    return (87, 80, 19)


def func5():
    return 44.5


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
