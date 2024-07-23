# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 69.35


def func2():
    return (36, 75, 87)


def func3():
    return 52


def func4():
    return {'fhoyz': 97, 'caela': 82, 'ovyns': 16}


def func5():
    return 'jjmhg'


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
