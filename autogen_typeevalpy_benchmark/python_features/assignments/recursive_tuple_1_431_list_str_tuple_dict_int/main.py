# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [51, 93, 90]


def func2():
    return 'lzypj'


def func3():
    return (41, 100, 53)


def func4():
    return {'evpem': 81, 'sfcvl': 52, 'eivjx': 100}


def func5():
    return 47


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
