# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [64, 65, 46]


def func2():
    return (80, 21, 61)


def func3():
    return 66


def func4():
    return {'dfpwg': 20, 'azyol': 83, 'bnlep': 98}


def func5():
    return 'ylzis'


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
