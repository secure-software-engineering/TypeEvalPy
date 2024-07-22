# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [33, 50, 61]


def func2():
    return {'ztvao': 58, 'drsjs': 78, 'ojsag': 77}


def func3():
    return 4


def func4():
    return (2, 91, 91)


def func5():
    return 'rtwvh'


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
