# Check if tool type coerces integer and string values.


def func1():
    return [4, 46, 44]


def func2():
    return (41, 83, 62)


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
