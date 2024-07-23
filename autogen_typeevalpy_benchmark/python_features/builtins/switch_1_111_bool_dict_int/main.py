#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return {'uogtm': 34, 'dnydf': 97, 'ylzcq': 24}
        case {'uogtm': 34, 'dnydf': 97, 'ylzcq': 24}:
            return False
        case _:
            return "default"


a = func(False)
b = func({'uogtm': 34, 'dnydf': 97, 'ylzcq': 24})
c = func(6)
