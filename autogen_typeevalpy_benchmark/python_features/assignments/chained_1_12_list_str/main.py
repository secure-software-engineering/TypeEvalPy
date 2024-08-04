# Two variables are assigned a function via chained assignment.


def func1():
    return [70, 8, 96]


def func2():
    return 'ibmxn'


a = b = func1

c = b()

a = b = func2

d = a()
