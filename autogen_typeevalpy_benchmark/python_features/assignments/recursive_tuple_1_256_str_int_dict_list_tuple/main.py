# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'hwgtk'


def func2():
    return 26


def func3():
    return {'yomdz': 19, 'mcfve': 57, 'tugpl': 77}


def func4():
    return [99, 6, 85]


def func5():
    return (65, 99, 25)


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
