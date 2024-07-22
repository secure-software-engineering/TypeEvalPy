# Check if tool type coerces integer and string values.


def func1():
    return (70, 58, 77)


def func2():
    return 13.66


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
