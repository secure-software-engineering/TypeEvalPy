# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'odazs'


def func2():
    return (63, 40, 48)


def func3():
    return {'giagi': 18, 'hijud': 22, 'dlcaf': 95}


def func4():
    return 57


def func5():
    return 44.91


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
