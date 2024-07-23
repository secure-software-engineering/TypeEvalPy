# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'glaut'


def func2():
    return [70, 20, 33]


def func3():
    return (18, 78, 11)


def func4():
    return {'kxhbo': 91, 'fpapi': 34, 'iclhg': 10}


def func5():
    return 44.48


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
