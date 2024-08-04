#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [1, 4, 71]:
            return 78.26
        case 78.26:
            return [1, 4, 71]
        case _:
            return "default"


a = func([1, 4, 71])
b = func(78.26)
c = func({'lnouc': 63, 'gseuj': 69, 'aosaw': 28})
