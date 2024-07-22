# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'kjebp': 36, 'jtkse': 56, 'nqigl': 34}


def func2():
    return 60.03


def func3():
    return (40, 76, 26)


def func4():
    return [34, 5, 58]


def func5():
    return 85


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
