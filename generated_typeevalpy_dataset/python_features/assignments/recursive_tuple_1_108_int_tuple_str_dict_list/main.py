# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 47


def func2():
    return (80, 4, 2)


def func3():
    return 'rpvjl'


def func4():
    return {'azott': 16, 'bxbwz': 69, 'rgzwa': 71}


def func5():
    return [60, 23, 12]


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
