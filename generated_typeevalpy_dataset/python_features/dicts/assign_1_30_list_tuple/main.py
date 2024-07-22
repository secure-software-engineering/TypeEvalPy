# A dictionary key is assigned to a function.


def func1():
    return [63, 67, 71]


def func2():
    return (74, 91, 94)


d = {"a": func1}

d["a"] = func2

e = d["a"]()
