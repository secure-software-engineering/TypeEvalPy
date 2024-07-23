# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'qamhy': 53, 'nqorj': 40, 'siggl': 16}


def func2():
    return (71, 4, 76)


def func3():
    return 'ciwhj'


def func4():
    return 81


def func5():
    return 10.79


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
