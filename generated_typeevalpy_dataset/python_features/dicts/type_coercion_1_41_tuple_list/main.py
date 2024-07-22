# Check if tool type coerces integer and string values.


def func1():
    return (55, 30, 15)


def func2():
    return [21, 14, 5]


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
