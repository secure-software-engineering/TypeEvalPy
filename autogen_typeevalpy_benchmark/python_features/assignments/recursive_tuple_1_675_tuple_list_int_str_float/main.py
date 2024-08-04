# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (95, 17, 76)


def func2():
    return [93, 17, 69]


def func3():
    return 52


def func4():
    return 'hqgfy'


def func5():
    return 81.38


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
