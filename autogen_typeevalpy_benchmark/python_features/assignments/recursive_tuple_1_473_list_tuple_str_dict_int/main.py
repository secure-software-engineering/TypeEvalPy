# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [35, 12, 50]


def func2():
    return (17, 83, 79)


def func3():
    return 'xihpa'


def func4():
    return {'ruzjd': 35, 'nrrqs': 73, 'omytn': 82}


def func5():
    return 93


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
