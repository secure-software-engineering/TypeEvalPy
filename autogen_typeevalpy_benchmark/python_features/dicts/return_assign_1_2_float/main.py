# A dictionary key is assigned to the returned value of a function.


def func2():
    return 83.84


def func1():
    return func2


d = {"a": func1()}

e = d["a"]()
