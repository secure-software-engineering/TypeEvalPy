#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'cdpda': 39, 'umawr': 77, 'kwxik': 96}:
            return 1.8
        case 1.8:
            return {'cdpda': 39, 'umawr': 77, 'kwxik': 96}
        case _:
            return "default"


a = func({'cdpda': 39, 'umawr': 77, 'kwxik': 96})
b = func(1.8)
c = func('zncck')
