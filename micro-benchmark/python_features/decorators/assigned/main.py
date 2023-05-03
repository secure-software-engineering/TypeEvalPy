# A decorator as a variable that has been assigned to function(s).


def dec1(f):
    return func2


def func2():
    return 42


a = dec1


@a
def func():
    return "Hello from func"


c = func()
