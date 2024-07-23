# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'zkfqu': 41, 'uzvjp': 9, 'uynim': 91}


def func2():
    return (40, 41, 69)


def func3():
    return [28, 61, 23]


def func4():
    return 70


def func5():
    return 'iyrmy'


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
