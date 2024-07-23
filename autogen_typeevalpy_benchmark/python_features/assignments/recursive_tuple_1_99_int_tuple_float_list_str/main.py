# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 7


def func2():
    return (31, 91, 15)


def func3():
    return 41.96


def func4():
    return [93, 96, 24]


def func5():
    return 'xggvz'


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
