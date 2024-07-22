# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'sxxyz'


def func2():
    return (50, 7, 4)


def func3():
    return 17.72


def func4():
    return {'jfeen': 77, 'ltzxm': 83, 'uzjby': 25}


def func5():
    return [6, 28, 73]


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
