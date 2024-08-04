# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 47.7


def func2():
    return [39, 65, 98]


def func3():
    return {'dojkm': 72, 'innwv': 57, 'yyvsv': 63}


def func4():
    return 89


def func5():
    return (33, 88, 16)


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
