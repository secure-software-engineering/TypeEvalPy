# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 4


def func2():
    return [68, 44, 4]


def func3():
    return {'ofcfq': 79, 'vsqvy': 9, 'yovnq': 21}


def func4():
    return 'gqfhd'


def func5():
    return (87, 50, 70)


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
