# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (63, 60, 7)


def func2():
    return 'jyodp'


def func3():
    return {'yfsic': 88, 'ebqul': 14, 'xyagf': 25}


def func4():
    return [3, 56, 42]


def func5():
    return 32.31


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
