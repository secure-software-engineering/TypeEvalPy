# A new list is created as a slice of another one containing functions.


def func1():
    return False


def func2():
    return {'nvtry': 69, 'oobsi': 60, 'swfcr': 46}


def func3():
    return 48.74


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
