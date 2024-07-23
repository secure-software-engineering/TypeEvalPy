# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [69, 92, 21]


def func2():
    return (85, 66, 96)


def func3():
    return 53


def func4():
    return {'uievd': 85, 'bwayv': 19, 'rtjxa': 85}


def func5():
    return 90.57


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
