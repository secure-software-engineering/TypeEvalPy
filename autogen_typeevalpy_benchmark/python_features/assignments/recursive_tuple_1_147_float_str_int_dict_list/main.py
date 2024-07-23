# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 84.84


def func2():
    return 'cbgpk'


def func3():
    return 4


def func4():
    return {'tcjfn': 70, 'jcldm': 85, 'fjmif': 32}


def func5():
    return [72, 4, 75]


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
