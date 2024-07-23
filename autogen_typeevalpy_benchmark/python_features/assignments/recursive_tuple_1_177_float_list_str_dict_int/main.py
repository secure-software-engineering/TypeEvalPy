# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 18.43


def func2():
    return [33, 62, 42]


def func3():
    return 'tzvkf'


def func4():
    return {'zigea': 32, 'dbumi': 31, 'pyeqs': 46}


def func5():
    return 83


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
