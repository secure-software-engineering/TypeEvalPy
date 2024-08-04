#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'rmfrg': 70, 'qwzkc': 7, 'jyhsk': 49}:
            return False
        case False:
            return {'rmfrg': 70, 'qwzkc': 7, 'jyhsk': 49}
        case _:
            return "default"


a = func({'rmfrg': 70, 'qwzkc': 7, 'jyhsk': 49})
b = func(False)
c = func((22, 65, 71))
