# Functions are assigned to variables via starred assignment
def func1():
    return [18, 68, 94]


def func2():
    return {'xyege': 75, 'maloc': 72, 'lzeki': 46}


def func3():
    return (59, 44, 87)


def func4():
    return 'exobp'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
