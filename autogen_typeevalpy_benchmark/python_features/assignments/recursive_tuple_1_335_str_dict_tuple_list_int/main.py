# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'itdcy'


def func2():
    return {'axbvk': 3, 'ceyxg': 61, 'iexsc': 28}


def func3():
    return (94, 91, 17)


def func4():
    return [22, 95, 88]


def func5():
    return 66


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
