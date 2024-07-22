# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 40.12


def func2():
    return {'yolgk': 49, 'krnrg': 11, 'yxczy': 72}


def func3():
    return 'jypfq'


def func4():
    return 60


def func5():
    return (22, 43, 37)


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
