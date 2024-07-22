# Check if tool type coerces integer and string values.


def func1():
    return 'agnqo'


def func2():
    return (18, 34, 53)


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
