# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'jtnml'


def func2():
    return (72, 3, 89)


def func3():
    return 8.55


def func4():
    return 73


def func5():
    return [18, 30, 53]


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
