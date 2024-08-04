# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 66.76


def func2():
    return {'rqqnn': 98, 'fkthy': 60, 'ewkav': 84}


def func3():
    return 'exjqz'


def func4():
    return (53, 25, 82)


def func5():
    return 4


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
