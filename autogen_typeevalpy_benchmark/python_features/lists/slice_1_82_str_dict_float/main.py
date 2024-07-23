# A new list is created as a slice of another one containing functions.


def func1():
    return 'bofpd'


def func2():
    return {'zywxs': 56, 'ddlad': 43, 'owaax': 80}


def func3():
    return 68.41


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
