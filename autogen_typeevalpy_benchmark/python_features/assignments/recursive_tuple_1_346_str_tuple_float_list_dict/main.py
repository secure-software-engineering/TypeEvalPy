# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'cnfoa'


def func2():
    return (90, 45, 46)


def func3():
    return 75.58


def func4():
    return [72, 90, 22]


def func5():
    return {'acqah': 18, 'eettf': 5, 'fdlrf': 16}


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
