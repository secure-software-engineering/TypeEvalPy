# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (68, 28, 73)


def func2():
    return [24, 8, 5]


def func3():
    return 'hdiie'


def func4():
    return {'pweav': 64, 'didte': 24, 'khqzf': 91}


def func5():
    return 42


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
