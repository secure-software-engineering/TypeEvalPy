# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [74, 90, 22]


def func2():
    return 46.7


def func3():
    return {'vxgya': 78, 'qvxgw': 38, 'rdrns': 37}


def func4():
    return 'fnpae'


def func5():
    return (75, 30, 79)


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
