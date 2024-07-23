#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 87:
            return 'wdrbd'
        case 'wdrbd':
            return 87
        case _:
            return "default"


a = func(87)
b = func('wdrbd')
c = func({'mnlez': 29, 'jwdys': 47, 'rqxfe': 24})
