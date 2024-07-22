# Check if tool type coerces integer and string values.


def func1():
    return 'jfzdu'


def func2():
    return [44, 13, 5]


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
