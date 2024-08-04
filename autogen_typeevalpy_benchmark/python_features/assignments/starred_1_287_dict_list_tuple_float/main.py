# Functions are assigned to variables via starred assignment
def func1():
    return {'akpnw': 23, 'zcasl': 84, 'ygbvy': 92}


def func2():
    return [97, 63, 9]


def func3():
    return (69, 53, 82)


def func4():
    return 65.22

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
