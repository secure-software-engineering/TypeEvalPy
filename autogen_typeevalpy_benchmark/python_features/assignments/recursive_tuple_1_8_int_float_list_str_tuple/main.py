# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 19


def func2():
    return 70.33


def func3():
    return [58, 83, 27]


def func4():
    return 'xqqli'


def func5():
    return (84, 52, 100)


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
