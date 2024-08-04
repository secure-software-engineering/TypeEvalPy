# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 5.22


def func2():
    return 46


def func3():
    return (18, 60, 93)


def func4():
    return [59, 36, 2]


def func5():
    return 'zjwnj'


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
