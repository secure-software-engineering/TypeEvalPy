# Functions are assigned as elements of a list and then called.


def func1():
    return [93, 97, 30]


def func2():
    return {'yiils': 9, 'spook': 52, 'hwwkp': 100}


def func3():
    return (76, 10, 69)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 17.85


b = ["Hello"]
b[0] = func4

f = b[0]()
