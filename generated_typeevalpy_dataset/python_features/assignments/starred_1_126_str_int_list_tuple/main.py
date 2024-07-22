# Functions are assigned to variables via starred assignment
def func1():
    return 'uwjae'


def func2():
    return 77


def func3():
    return [78, 68, 81]


def func4():
    return (22, 70, 11)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
