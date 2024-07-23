# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [56, 83, 87]


def func2():
    return 67.41


def func3():
    return 'fntvy'


def func4():
    return (52, 19, 94)


def func5():
    return {'vcfgw': 47, 'ssfrc': 17, 'tgznc': 43}


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
