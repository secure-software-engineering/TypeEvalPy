# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [69, 47, 99]


def func2():
    return 'owftt'


def func3():
    return 57.1


def func4():
    return (65, 42, 70)


def func5():
    return {'eaaiu': 46, 'orqsn': 10, 'jcgny': 13}


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
