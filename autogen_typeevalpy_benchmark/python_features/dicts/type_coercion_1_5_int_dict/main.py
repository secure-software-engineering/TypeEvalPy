# Check if tool type coerces integer and string values.


def func1():
    return 76


def func2():
    return {'aftkl': 80, 'sqtxt': 92, 'yzvap': 80}


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
