# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (54, 90, 19)


def func2():
    return 75


def func3():
    return 'xaidu'


def func4():
    return [66, 26, 17]


def func5():
    return 51.84


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
