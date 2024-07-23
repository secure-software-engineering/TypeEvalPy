# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 4


def func2():
    return [12, 10, 45]


def func3():
    return 87.43


def func4():
    return {'fttgz': 94, 'mnpko': 18, 'qicpi': 63}


def func5():
    return (95, 29, 65)


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
