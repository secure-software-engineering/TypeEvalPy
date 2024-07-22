# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'dudhk': 35, 'luhxw': 21, 'lqkgt': 70}


def func2():
    return (59, 44, 12)


def func3():
    return 'pbcjj'


def func4():
    return 34.75


def func5():
    return [52, 45, 68]


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
