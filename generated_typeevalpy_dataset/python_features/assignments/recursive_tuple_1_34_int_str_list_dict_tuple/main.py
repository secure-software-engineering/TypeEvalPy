# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 79


def func2():
    return 'nexsr'


def func3():
    return [20, 17, 24]


def func4():
    return {'jhxom': 6, 'xhxif': 46, 'ugfbs': 36}


def func5():
    return (62, 79, 71)


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
