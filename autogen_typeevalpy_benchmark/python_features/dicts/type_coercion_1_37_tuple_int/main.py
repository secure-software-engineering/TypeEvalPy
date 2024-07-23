# Check if tool type coerces integer and string values.


def func1():
    return (26, 28, 96)


def func2():
    return 1


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
