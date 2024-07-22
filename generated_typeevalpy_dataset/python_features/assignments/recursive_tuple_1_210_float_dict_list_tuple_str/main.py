# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 5.58


def func2():
    return {'umedw': 66, 'cljbu': 14, 'tzmet': 89}


def func3():
    return [74, 34, 52]


def func4():
    return (81, 6, 10)


def func5():
    return 'fhipq'


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
