# Check if tool type coerces integer and string values.


def func1():
    return (69, 99, 31)


def func2():
    return [26, 45, 78]


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
