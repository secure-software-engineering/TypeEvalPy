# A dictionary key is assigned to a function.


def func1():
    return True


def func2():
    return 'wnpek'


d = {"a": func1}

d["a"] = func2

e = d["a"]()
