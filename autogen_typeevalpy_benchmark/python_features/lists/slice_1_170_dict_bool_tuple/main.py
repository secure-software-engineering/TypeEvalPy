# A new list is created as a slice of another one containing functions.


def func1():
    return {'xrrxi': 18, 'boeph': 4, 'jfapt': 73}


def func2():
    return False


def func3():
    return (56, 84, 44)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
