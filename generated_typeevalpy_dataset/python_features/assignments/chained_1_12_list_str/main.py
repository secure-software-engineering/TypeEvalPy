# Two variables are assigned a function via chained assignment.


def func1():
    return [11, 86, 43]


def func2():
    return 'llrzv'


a = b = func1

c = b()

a = b = func2

d = a()
