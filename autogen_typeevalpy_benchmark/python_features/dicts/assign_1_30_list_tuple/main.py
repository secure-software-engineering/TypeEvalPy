# A dictionary key is assigned to a function.


def func1():
    return [83, 53, 87]


def func2():
    return (2, 94, 42)


d = {"a": func1}

d["a"] = func2

e = d["a"]()
