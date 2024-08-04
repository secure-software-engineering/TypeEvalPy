# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'promc'


def func2():
    return [63, 44, 69]


def func3():
    return {'nqggh': 53, 'hnixx': 36, 'ojhvn': 34}


def func4():
    return 60.18


def func5():
    return 86


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
