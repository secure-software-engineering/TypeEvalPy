# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 70.92


def func2():
    return 50


def func3():
    return (66, 9, 23)


def func4():
    return [84, 20, 46]


def func5():
    return {'rolwd': 65, 'urybv': 100, 'mzpes': 85}


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
