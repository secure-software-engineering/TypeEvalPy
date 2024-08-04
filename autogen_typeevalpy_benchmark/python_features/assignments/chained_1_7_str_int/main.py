# Two variables are assigned a function via chained assignment.


def func1():
    return 'qoact'


def func2():
    return 31


a = b = func1

c = b()

a = b = func2

d = a()
