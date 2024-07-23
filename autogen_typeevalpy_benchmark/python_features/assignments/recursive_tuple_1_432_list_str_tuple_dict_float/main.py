# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [1, 3, 25]


def func2():
    return 'zeoxl'


def func3():
    return (75, 43, 5)


def func4():
    return {'phyfn': 10, 'eyxtz': 74, 'asshx': 80}


def func5():
    return 1.01


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
