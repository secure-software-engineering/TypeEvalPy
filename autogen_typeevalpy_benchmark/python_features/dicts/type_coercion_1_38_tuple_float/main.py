# Check if tool type coerces integer and string values.


def func1():
    return (91, 68, 6)


def func2():
    return 48.98


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
