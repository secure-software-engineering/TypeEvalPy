# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 65.22


def func2():
    return 'jshxw'


def func3():
    return (63, 100, 20)


def func4():
    return [51, 53, 49]


def func5():
    return {'uzewy': 55, 'ghgha': 42, 'kuium': 28}


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
