# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'zmcbz': 63, 'bepud': 16, 'newjc': 20}


def func2():
    return 51


def func3():
    return 10.88


def func4():
    return [83, 71, 29]


def func5():
    return (72, 87, 72)


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
