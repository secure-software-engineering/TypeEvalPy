# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 62.8


def func2():
    return (38, 43, 79)


def func3():
    return [60, 61, 80]


def func4():
    return {'hovwb': 62, 'qwxvt': 59, 'pjxop': 53}


def func5():
    return 'fjiqa'


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
