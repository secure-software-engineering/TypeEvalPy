# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (63, 18, 35)


def func2():
    return 'idgfk'


def func3():
    return 27.76


def func4():
    return [2, 39, 41]


def func5():
    return {'xmjut': 75, 'mzzai': 81, 'qyorx': 98}


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
