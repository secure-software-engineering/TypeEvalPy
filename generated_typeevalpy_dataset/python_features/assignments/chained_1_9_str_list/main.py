# Two variables are assigned a function via chained assignment.


def func1():
    return 'lcoea'


def func2():
    return [15, 32, 37]


a = b = func1

c = b()

a = b = func2

d = a()
