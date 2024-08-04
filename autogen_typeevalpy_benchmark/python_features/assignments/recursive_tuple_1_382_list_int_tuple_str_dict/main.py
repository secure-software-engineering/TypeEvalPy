# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [17, 5, 43]


def func2():
    return 5


def func3():
    return (78, 89, 94)


def func4():
    return 'fvlss'


def func5():
    return {'gzqhp': 5, 'vpobc': 89, 'jqnzt': 84}


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
