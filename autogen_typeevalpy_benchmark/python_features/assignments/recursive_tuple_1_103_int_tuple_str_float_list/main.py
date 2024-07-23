# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 77


def func2():
    return (22, 3, 3)


def func3():
    return 'ghtsv'


def func4():
    return 92.59


def func5():
    return [84, 7, 12]


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
