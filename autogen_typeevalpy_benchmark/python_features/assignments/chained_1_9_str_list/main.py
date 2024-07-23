# Two variables are assigned a function via chained assignment.


def func1():
    return 'kydgi'


def func2():
    return [66, 100, 50]


a = b = func1

c = b()

a = b = func2

d = a()
