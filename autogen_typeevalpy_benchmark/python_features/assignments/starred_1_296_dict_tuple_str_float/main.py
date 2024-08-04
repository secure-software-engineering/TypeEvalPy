# Functions are assigned to variables via starred assignment
def func1():
    return {'ppvyk': 66, 'akqpf': 4, 'cybwg': 89}


def func2():
    return (16, 31, 93)


def func3():
    return 'ymwjo'


def func4():
    return 25.53

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
