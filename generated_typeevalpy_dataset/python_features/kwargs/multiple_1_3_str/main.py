# Call a function with keyword arguments.


def concatenate(**kwargs):
    result = 'nocti'
    for arg in kwargs.values():
        result += arg
    return result


c = concatenate(a='nocti', b='nocti', c='nocti')
