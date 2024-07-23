# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 52


def func2():
    return 75.62


def func3():
    return {'fmzso': 81, 'johiq': 84, 'vruiu': 96}


def func4():
    return [72, 49, 21]


def func5():
    return (74, 56, 27)


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
