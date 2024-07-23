# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (22, 60, 66)


def func2():
    return 10


def func3():
    return {'xlvpu': 74, 'mptyg': 24, 'karyt': 73}


def func4():
    return 25.29


def func5():
    return [62, 22, 79]


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
