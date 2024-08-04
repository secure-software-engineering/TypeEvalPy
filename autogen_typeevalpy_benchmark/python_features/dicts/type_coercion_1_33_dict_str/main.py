# Check if tool type coerces integer and string values.


def func1():
    return {'zgmhs': 78, 'clkcn': 82, 'tgqhh': 26}


def func2():
    return 'dnsna'


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
