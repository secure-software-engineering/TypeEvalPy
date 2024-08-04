# Two variables are assigned a function via chained assignment.


def func1():
    return 60


def func2():
    return 'wbqqb'


a = b = func1

c = b()

a = b = func2

d = a()
