# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 70


def func2():
    return 'mjxnk'


def func3():
    return {'zfott': 23, 'otrnr': 36, 'rinhw': 7}


def func4():
    return 15.25


def func5():
    return [86, 29, 77]


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
