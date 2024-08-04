# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'axorv': 89, 'nadmt': 66, 'smyca': 15}


def func2():
    return [100, 79, 61]


def func3():
    return 'zexrw'


def func4():
    return 59.22


def func5():
    return (50, 33, 62)


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
