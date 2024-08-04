# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'fkcvb': 20, 'fjlrf': 100, 'mdkse': 5}


def func2():
    return 'aiuku'


def func3():
    return [93, 18, 9]


def func4():
    return (74, 47, 26)


def func5():
    return 41.52


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
