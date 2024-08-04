# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'dbtnw'


def func2():
    return (72, 62, 51)


def func3():
    return [84, 75, 92]


def func4():
    return 95


def func5():
    return 81.85


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
