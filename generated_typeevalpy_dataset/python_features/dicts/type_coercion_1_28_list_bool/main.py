# Check if tool type coerces integer and string values.


def func1():
    return [38, 72, 44]


def func2():
    return True


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
