# A dictionary key is assigned to a function.


def func1():
    return 'fdmcu'


def func2():
    return (3, 40, 23)


d = {"a": func1}

d["a"] = func2

e = d["a"]()
