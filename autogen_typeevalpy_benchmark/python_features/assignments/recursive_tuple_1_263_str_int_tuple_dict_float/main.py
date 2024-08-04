# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'digtt'


def func2():
    return 63


def func3():
    return (41, 79, 98)


def func4():
    return {'ptwru': 9, 'cawbw': 47, 'ixfdf': 80}


def func5():
    return 91.02


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
