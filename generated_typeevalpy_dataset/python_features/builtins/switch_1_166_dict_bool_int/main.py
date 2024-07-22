#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'nalen': 85, 'hdqxj': 41, 'kqroo': 31}:
            return False
        case False:
            return {'nalen': 85, 'hdqxj': 41, 'kqroo': 31}
        case _:
            return "default"


a = func({'nalen': 85, 'hdqxj': 41, 'kqroo': 31})
b = func(False)
c = func(8)
