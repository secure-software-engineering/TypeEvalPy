#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'pewez': 5, 'qvxju': 23, 'howal': 54}:
            return False
        case False:
            return {'pewez': 5, 'qvxju': 23, 'howal': 54}
        case _:
            return "default"


a = func({'pewez': 5, 'qvxju': 23, 'howal': 54})
b = func(False)
c = func(74.88)
