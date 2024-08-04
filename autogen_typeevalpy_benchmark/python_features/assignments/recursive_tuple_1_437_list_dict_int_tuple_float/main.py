# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [43, 92, 82]


def func2():
    return {'fkzzi': 82, 'ovgxi': 95, 'fhaxs': 14}


def func3():
    return 66


def func4():
    return (9, 92, 51)


def func5():
    return 44.61


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
