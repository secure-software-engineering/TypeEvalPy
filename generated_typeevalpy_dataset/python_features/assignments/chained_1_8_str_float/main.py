# Two variables are assigned a function via chained assignment.


def func1():
    return 'odfnk'


def func2():
    return 24.84


a = b = func1

c = b()

a = b = func2

d = a()
