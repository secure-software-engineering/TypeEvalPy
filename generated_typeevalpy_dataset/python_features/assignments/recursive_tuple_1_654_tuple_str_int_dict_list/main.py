# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (74, 40, 60)


def func2():
    return 'gasll'


def func3():
    return 82


def func4():
    return {'dgkci': 81, 'btaow': 75, 'jkmyu': 49}


def func5():
    return [93, 100, 43]


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
