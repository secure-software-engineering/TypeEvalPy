# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'wetnq': 48, 'ividg': 60, 'ddqgo': 34}


def func2():
    return (69, 58, 76)


def func3():
    return [34, 79, 2]


def func4():
    return 74


def func5():
    return 'rcldi'


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
