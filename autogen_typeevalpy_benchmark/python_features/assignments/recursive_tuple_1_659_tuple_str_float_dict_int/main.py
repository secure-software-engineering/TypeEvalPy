# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (34, 90, 69)


def func2():
    return 'nmyjm'


def func3():
    return 26.72


def func4():
    return {'frkku': 13, 'dcdau': 89, 'ghfkd': 28}


def func5():
    return 63


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
