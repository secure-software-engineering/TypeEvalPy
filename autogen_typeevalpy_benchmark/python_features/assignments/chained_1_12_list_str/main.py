# Two variables are assigned a function via chained assignment.


def func1():
    return [63, 26, 69]


def func2():
    return 'jmwyt'


a = b = func1

c = b()

a = b = func2

d = a()
