# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 9.61


def func2():
    return 70


def func3():
    return [35, 12, 59]


def func4():
    return {'eghln': 74, 'ifaxw': 94, 'oumyh': 38}


def func5():
    return (85, 95, 42)


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
