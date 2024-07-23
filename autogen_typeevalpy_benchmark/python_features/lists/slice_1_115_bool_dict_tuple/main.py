# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return {'obykq': 37, 'zbzno': 95, 'ohmdl': 78}


def func3():
    return (80, 4, 91)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
