# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (17, 18, 18)


def func2():
    return [36, 5, 5]


def func3():
    return 'zgzdr'


def func4():
    return 7


def func5():
    return {'jdayt': 67, 'twcfn': 49, 'fofqj': 15}


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
