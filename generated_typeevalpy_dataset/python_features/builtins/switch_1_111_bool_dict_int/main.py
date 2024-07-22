#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return {'jydyd': 32, 'xhrdn': 3, 'ohqmv': 63}
        case {'jydyd': 32, 'xhrdn': 3, 'ohqmv': 63}:
            return True
        case _:
            return "default"


a = func(True)
b = func({'jydyd': 32, 'xhrdn': 3, 'ohqmv': 63})
c = func(10)
