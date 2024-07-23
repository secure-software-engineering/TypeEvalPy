# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (87, 84, 7)


def func2():
    return [99, 51, 97]


def func3():
    return {'ibiub': 65, 'tezdi': 92, 'xwsxe': 9}


def func4():
    return 'rmlfq'


def func5():
    return 70


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
