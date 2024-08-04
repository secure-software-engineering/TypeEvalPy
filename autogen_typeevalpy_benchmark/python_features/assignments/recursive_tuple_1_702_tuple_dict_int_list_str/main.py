# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (100, 65, 38)


def func2():
    return {'xweqc': 84, 'ektjj': 36, 'gwmrc': 15}


def func3():
    return 29


def func4():
    return [1, 49, 66]


def func5():
    return 'qywgu'


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
