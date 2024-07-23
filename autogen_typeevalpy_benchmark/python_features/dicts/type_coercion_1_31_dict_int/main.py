# Check if tool type coerces integer and string values.


def func1():
    return {'fwyqh': 72, 'dmcia': 5, 'focsp': 44}


def func2():
    return 27


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
