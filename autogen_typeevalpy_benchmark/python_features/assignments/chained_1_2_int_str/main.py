# Two variables are assigned a function via chained assignment.


def func1():
    return 87


def func2():
    return 'zuusg'


a = b = func1

c = b()

a = b = func2

d = a()
