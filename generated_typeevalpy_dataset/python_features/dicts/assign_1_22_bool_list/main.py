# A dictionary key is assigned to a function.


def func1():
    return False


def func2():
    return [14, 23, 73]


d = {"a": func1}

d["a"] = func2

e = d["a"]()
