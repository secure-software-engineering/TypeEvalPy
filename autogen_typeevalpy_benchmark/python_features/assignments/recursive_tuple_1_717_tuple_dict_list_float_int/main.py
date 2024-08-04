# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (82, 67, 93)


def func2():
    return {'hnkxc': 69, 'hdiaa': 73, 'tlixo': 90}


def func3():
    return [20, 32, 90]


def func4():
    return 70.03


def func5():
    return 27


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
