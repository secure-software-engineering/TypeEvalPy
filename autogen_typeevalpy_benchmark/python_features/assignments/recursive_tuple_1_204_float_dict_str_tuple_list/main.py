# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 62.27


def func2():
    return {'dqzpt': 71, 'yigom': 66, 'cjtwr': 25}


def func3():
    return 'wejwe'


def func4():
    return (92, 26, 42)


def func5():
    return [17, 38, 9]


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
