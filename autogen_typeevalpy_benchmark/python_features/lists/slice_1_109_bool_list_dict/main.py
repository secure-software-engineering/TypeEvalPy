# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return [70, 75, 68]


def func3():
    return {'xnsbt': 43, 'elkhn': 91, 'wmjvy': 30}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
