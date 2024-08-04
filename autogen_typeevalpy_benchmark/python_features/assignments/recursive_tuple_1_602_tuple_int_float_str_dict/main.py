# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (53, 97, 55)


def func2():
    return 5


def func3():
    return 34.41


def func4():
    return 'aslxp'


def func5():
    return {'gamlf': 74, 'vmuxo': 83, 'dtkxm': 36}


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
