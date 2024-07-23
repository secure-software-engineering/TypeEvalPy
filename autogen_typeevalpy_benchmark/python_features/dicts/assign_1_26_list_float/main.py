# A dictionary key is assigned to a function.


def func1():
    return [93, 41, 56]


def func2():
    return 92.61


d = {"a": func1}

d["a"] = func2

e = d["a"]()
