# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'cpkri': 55, 'frilk': 74, 'jjwxg': 98}


def func2():
    return 48


def func3():
    return [15, 12, 69]


def func4():
    return 22.36


def func5():
    return (45, 64, 30)


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
