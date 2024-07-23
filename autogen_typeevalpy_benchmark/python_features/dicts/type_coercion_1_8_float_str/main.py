# Check if tool type coerces integer and string values.


def func1():
    return 80.83


def func2():
    return 'bzhct'


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
