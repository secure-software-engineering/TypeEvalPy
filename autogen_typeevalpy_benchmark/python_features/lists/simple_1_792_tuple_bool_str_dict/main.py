# Functions are assigned as elements of a list and then called.


def func1():
    return (81, 27, 92)


def func2():
    return True


def func3():
    return 'bwvcc'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'jcxzw': 59, 'pvhma': 87, 'yqspr': 52}


b = ["Hello"]
b[0] = func4

f = b[0]()
