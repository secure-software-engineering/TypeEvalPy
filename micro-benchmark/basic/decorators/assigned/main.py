# A decorator as a variable that has been assigned to function(s).

def dec1(f):
    return f


def dec2(f):
    return f


a = dec1
a = dec2


@a
def func():
    return "Hello from func"


a = func()
