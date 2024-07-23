# Functions are assigned to variables via starred assignment
def func1():
    return 87.3


def func2():
    return 'vwywu'


def func3():
    return {'zpxgi': 25, 'hlxez': 45, 'shtvi': 72}


def func4():
    return [26, 8, 93]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
