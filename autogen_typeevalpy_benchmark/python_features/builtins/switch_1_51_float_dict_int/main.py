#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 49.97:
            return {'scndj': 99, 'nztyg': 93, 'utqao': 79}
        case {'scndj': 99, 'nztyg': 93, 'utqao': 79}:
            return 49.97
        case _:
            return "default"


a = func(49.97)
b = func({'scndj': 99, 'nztyg': 93, 'utqao': 79})
c = func(11)
