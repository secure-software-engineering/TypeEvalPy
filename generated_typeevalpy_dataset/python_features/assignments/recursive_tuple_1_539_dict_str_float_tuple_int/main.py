# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'mblvc': 22, 'rjwcg': 54, 'ivkcx': 4}


def func2():
    return 'pywnl'


def func3():
    return 7.76


def func4():
    return (76, 2, 71)


def func5():
    return 73


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
