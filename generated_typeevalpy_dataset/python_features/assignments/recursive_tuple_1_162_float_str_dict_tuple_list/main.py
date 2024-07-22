# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 18.87


def func2():
    return 'kvfkv'


def func3():
    return {'odxom': 7, 'bgiae': 20, 'cvqxh': 30}


def func4():
    return (79, 84, 57)


def func5():
    return [38, 38, 5]


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
