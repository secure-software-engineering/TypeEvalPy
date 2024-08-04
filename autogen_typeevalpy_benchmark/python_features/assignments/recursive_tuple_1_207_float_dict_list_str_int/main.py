# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 17.73


def func2():
    return {'kixuf': 90, 'cqbxm': 34, 'gghlu': 73}


def func3():
    return [36, 77, 5]


def func4():
    return 'tdhfj'


def func5():
    return 47


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
