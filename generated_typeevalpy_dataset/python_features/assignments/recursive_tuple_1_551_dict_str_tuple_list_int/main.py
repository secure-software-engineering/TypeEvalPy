# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'fhhiw': 97, 'rnrek': 12, 'tqovl': 94}


def func2():
    return 'zipid'


def func3():
    return (63, 15, 28)


def func4():
    return [96, 82, 14]


def func5():
    return 43


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
